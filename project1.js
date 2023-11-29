import React, { useState } from 'react';

const choices = ['stone', 'paper', 'scissors'];

const App = () => {
  const [player1Choice, setPlayer1Choice] = useState(null);
  const [player2Choice, setPlayer2Choice] = useState(null);
  const [result, setResult] = useState('');

  const handleChoice = (choice) => {
    setPlayer1Choice(choice);
    const randomIndex = Math.floor(Math.random() * 3);
    const player2Choice = choices[randomIndex];
    setPlayer2Choice(player2Choice);
    calculateResult(choice, player2Choice);
  };

  const calculateResult = (player1Choice, player2Choice) => {
    if (player1Choice === player2Choice) {
      setResult('It\'s a tie!');
    } else if (
      (player1Choice === 'stone' && player2Choice === 'scissors') ||
      (player1Choice === 'paper' && player2Choice === 'stone') ||
      (player1Choice === 'scissors' && player2Choice === 'paper')
    ) {
      setResult('Player 1 wins!');
    } else {
      setResult('Player 2 wins!');
    }
  };

  return (
    <div>
      <h1>Stone, Paper, Scissors</h1>
      <div>
        {choices.map((choice) => (
          <button key={choice} onClick={() => handleChoice(choice)}>
            {choice}
          </button>
        ))}
      </div>
      <div>
        {player1Choice && (
          <>
            <p>Player 1's Choice: {player1Choice}</p>
            <p>Player 2's Choice: {player2Choice}</p>
            <p>Result: {result}</p>
          </>
        )}
      </div>
    </div>
  );
};

export default App;
