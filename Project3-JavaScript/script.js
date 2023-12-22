// Step 1: HTML and JavaScript Setup

// Step 3: Fetching the JSON File
fetch('data.json')
  .then(response => response.json())
  .then(data => {
    // Additional code to manipulate the data goes here
    displayData(data); // Call the function to display data in the browser
    logData(data); // Log data to the console
    logDataInfo(data); // Log data information to the console
  });

// Step 4: Displaying JSON Data
function displayData(data) {
  const container = document.createElement('div');

  data.forEach(item => {
    const element = document.createElement('p');
    element.textContent = `Name: ${item.name}, Age: ${item.age}`; // Modify as per your JSON structure
    container.appendChild(element);
  });

  document.body.appendChild(container);
}

// Step 5: Writing Functions to Describe JSON Data
function countRecords(data) {
  return `Total records: ${data.length}`;
}

function listKeys(data) {
  const keys = Object.keys(data[0]);
  return `Keys in the data: ${keys.join(', ')}`;
}

function describeData(data) {
  const totalRecords = countRecords(data);
  const keysList = listKeys(data);
  return `${totalRecords}\n${keysList}`;
}

// Log data to the console
function logData(data) {
  data.forEach(item => {
    console.log(`Name: ${item.name}, Age: ${item.age}`); // Log each item to the console
  });
}

// Log data information to the console
function logDataInfo(data) {
  console.log(countRecords(data));
  console.log(listKeys(data));
  console.log(describeData(data));
}
