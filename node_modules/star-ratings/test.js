// jshint mocha:true

var weightedAverage = require('./');
var assert  = require('assert');

describe('calculate', function() {

  it('should returned weighted average', function(){
    // [1-star-voters, 2-star-voters, 3-star-voters,...]
    var votes = [22, 45, 56, 77, 120];
    var rating = weightedAverage(votes);

    console.log(rating);

    assert.ok(rating);
  });

});
