# Star Rating

[![NPM](https://nodei.co/npm/star-ratings.png?downloads=true&stars=true)](https://nodei.co/npm/star-ratings/)

Calculate the Weighted Average to get a rating. Useful for calculating 5-star or more ratings

## example


```javascript

  var starRatings = require('star-ratings');

  // [1-star-voters, 2-star-voters, 3-star-voters, 4-star-voters, ...]
  var votes = [12, 234, 456, 767, 566];
  var rating = starRatings(votes);
  console.log(rating); // '3.8'
```

## API.

### starRatings(voters#Array)

Returns a `string` _rating_ that is the weighted average.

## install

```javascript
  $ npm install star-ratings
```

## license

MIT.
