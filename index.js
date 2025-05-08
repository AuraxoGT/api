const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/api/timestamp', (req, res) => {
  const dateParam = req.query.date;
  let date;

  if (!dateParam) {
    date = new Date();
  } else {
    date = isNaN(dateParam) ? new Date(dateParam) : new Date(parseInt(dateParam));
  }

  if (isNaN(date.getTime())) {
    return res.status(400).json({ error: 'Invalid Date' });
  }

  // Return the timestamp in seconds
  res.json({
    date: date.toISOString(),
    timestamp: Math.floor(date.getTime() / 1000)  // Convert to seconds
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
