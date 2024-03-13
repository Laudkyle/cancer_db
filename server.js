const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
const port = 3001;

// Create a MySQL connection
const db = mysql.createConnection({
  host: 'https://addlifetoyears.org/',
  user: 'addlifet_kyle',
  password: 'Tersely001@',
  database: 'addlifet_cancer1',
});

// Connect to the database
db.connect();

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// Define an API endpoint to fetch data from the database
app.get('/', (req, res) => {
  const sql = 'SELECT * FROM health';
  
  // Execute the SQL query
  db.query(sql, (err, result) => {
    if (err) throw err;
    res.json(result);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
