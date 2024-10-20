const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { promisify } = require('util');

const app = express();
const PORT = process.env.PORT || 3000;

// Set EJS as templating engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware to parse URL-encoded data (from HTML forms)
app.use(express.urlencoded({ extended: true }));

// Create uploads directory if it doesn't exist
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}
// Set up storage for multer
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const folderName = req.body.folder || 'default'; // Use the specified folder or 'default'
    const folderPath = path.join(uploadDir, folderName);

    // Create the folder if it doesn't exist
    if (!fs.existsSync(folderPath)) {
      fs.mkdirSync(folderPath, { recursive: true });
    }
    cb(null, folderPath);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname); // Keep original file name
  },
});

// Allow multiple file uploads
const upload = multer({ storage }).array('files'); // Ensure 'files' matches the form input name

// Serve static files from the public directory
app.use('/uploads', express.static(uploadDir));

// Route to render the upload form and list folders
app.get('/', (req, res) => {
  fs.readdir(uploadDir, (err, folders) => {
    if (err) {
      console.error('Error reading directory:', err);
      return res.status(500).send('Error reading directory');
    }

    res.render('index', { folders });
  });
});

// Route to render the upload form and list folders
app.get('/up', (req, res) => {
  fs.readdir(uploadDir, (err, folders) => {
    if (err) {
      console.error('Error reading directory:', err);
      return res.status(500).send('Error reading directory');
    }

    res.render('upload', { folders });
  });
});

// Route to render files in a specific folder
app.get('/folder/:folderName', (req, res) => {
  const folderPath = path.join(uploadDir, req.params.folderName);
  fs.readdir(folderPath, (err, files) => {
    if (err) {
      console.error('Error reading folder:', err);
      return res.status(500).send('Error reading folder');
    }
    res.render('folder', { folderName: req.params.folderName, files });
  });
});

// Route to handle file uploads
app.post('/upload', (req, res) => {
  upload(req, res, (err) => {
    if (err) {
      console.error('Error uploading files:', err);
      return res.status(500).send('Error uploading files');
    }

    // Count the number of uploaded files
    const fileCount = req.files.length; // Use .length to count the number of files

    console.log(`Files uploaded successfully: ${fileCount} files`);
    res.redirect('/up');
  });
});

// Route to download a file
app.get('/download/:folder/:filename', (req, res) => {
  const filePath = path.join(uploadDir, req.params.folder, req.params.filename);
  res.download(filePath, (err) => {
    if (err) {
      console.error('Error downloading file:', err);
      res.status(404).send('File not found');
    }
  });
});

// Route to empty the uploads directory
app.post('/empty-uploads', (req, res) => {
  fs.readdir(uploadDir, (err, folders) => {
    if (err) {
      console.error('Error reading uploads directory:', err);
      return res.status(500).send('Error reading uploads directory');
    }

    // Remove each folder and its contents
    const removePromises = folders.map((folder) => {
      const folderPath = path.join(uploadDir, folder);
      return new Promise((resolve, reject) => {
        fs.rm(folderPath, { recursive: true, force: true }, (err) => {
          if (err) {
            console.error(`Error removing folder ${folder}:`, err);
            return reject(err);
          }
          resolve();
        });
      });
    });

    // Wait for all folders to be deleted
    Promise.all(removePromises)
      .then(() => {
        console.log('All uploads emptied successfully');
        res.redirect('/');
      })
      .catch((err) => {
        console.error('Error emptying uploads:', err);
        res.status(500).send('Error emptying uploads directory');
      });
  });
});

// Route to delete a specific folder
app.post('/delete-folder/:folderName', (req, res) => {
  const folderPath = path.join(uploadDir, req.params.folderName);

  fs.rm(folderPath, { recursive: true, force: true }, (err) => {
    if (err) {
      console.error(`Error deleting folder ${req.params.folderName}:`, err);
      return res.status(500).send('Error deleting folder');
    }
    console.log(`Folder ${req.params.folderName} deleted successfully`);
    res.redirect('/');
  });
});



// API endpoint to search for a string in all files
app.get('/search=:searchString', async (req, res) => {
    const searchString = req.params.searchString;

    if (!searchString) {
        return res.status(400).json({ error: 'Search string is required' });
    }

    try {
        const matches = await searchFiles(uploadDir, searchString);
        // Format the results with line breaks
        const formattedResults = matches.join('\n'); // Join with line breaks
        res.type('text/plain').send(formattedResults); // Send as plain text for better readability
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Error searching files' });
    }
});

// Function to search for the string in files
const searchFiles = async (dir, searchString) => {
    const results = [];
    const files = await promisify(fs.readdir)(dir);

    for (const file of files) {
        const filePath = path.join(dir, file);
        const stat = await promisify(fs.stat)(filePath);

        if (stat.isDirectory()) {
            const subDirResults = await searchFiles(filePath, searchString);
            results.push(...subDirResults);
        } else {
            const content = await promisify(fs.readFile)(filePath, 'utf8');
            if (content.includes(searchString)) {
                // Construct the URL for the found file
                const relativePath = path.relative(uploadDir, filePath).replace(/\\/g, '/');
                const fullUrl = `http://localhost:3000/uploads/${relativePath}`;
                results.push('curl -O '+fullUrl);
            }
        }
    }

    return results;
};

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
