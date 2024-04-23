module.exports = function calculate(voters) {
  var total_per_rate = 0;
  var total_voters = 0;


  for(var i = 1; i <= voters.length; i++) {
    total_per_rate += (i * voters[i - 1]);
    total_voters += voters[i - 1];
  }


  return (total_per_rate / total_voters).toPrecision(2);
};
