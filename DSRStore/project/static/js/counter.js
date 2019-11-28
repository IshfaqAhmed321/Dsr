function increaseValue(valueid) {
  var value = parseInt(document.getElementById(valueid).value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  document.getElementById(valueid).value = value;
}

function decreaseValue(valueid) {
  var value = parseInt(document.getElementById(valueid).value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? value = 1 : '';
  value--;
  document.getElementById(valueid).value = value;
}
