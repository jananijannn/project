const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;


const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'examp',
}); 

db.connect((err) => {
  if (err) {
    console.error('MySQL connection error:', err);
    throw err;
  }
  console.log('Connected to MySQL');
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/api/players', (req, res) => {
  const { playerName, playerChoice } = req.body;

  const sql = 'INSERT INTO players (playerName, playerChoice) VALUES (?, ?)';
  const values = [playerName, playerChoice];

  db.query(sql, values, (err, result) => {
    if (err) {
      console.error('MySQL query error:', err);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }

    res.status(201).json({ message: 'Player details stored successfully.' });
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
