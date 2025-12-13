const input = $input.first().json;
const currentYear = new Date().getFullYear();
const fullDateStr = $input.first().json.completed_task[25].output_value + currentYear;

let dateObj = new Date(fullDateStr);

let isoDate = dateObj.toISOString();
// Create a Date object
dateObj = new Date(isoDate);

// Helper function to pad numbers
function pad(num) {
  return num.toString().padStart(2, "0");
}
// Store everything in variables
const day = dateObj.getDate();
const month = dateObj.getMonth() + 1; // Month is zero-indexed
const year = dateObj.getFullYear();
const hours = dateObj.getHours();
const minutes = dateObj.getMinutes();
const seconds = dateObj.getSeconds();


// Plug everything into final format
isoDate= `$pad(day)-$pad(month)-year $pad(hours):$pad(minutes):$pad(seconds)`;