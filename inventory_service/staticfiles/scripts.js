

const API_BASE = 'http://127.0.0.1:8000/';

// Select DOM Elements
const orderForm = document.getElementById('orderForm');
const productNameInput = document.getElementById('productName');
const quantityInput = document.getElementById('quantity');
const inventoryList = document.getElementById('inventoryList');
const loadingSpinner = document.getElementById('loadingSpinner');
const orderMessage = document.getElementById('orderMessage');
const refreshButton = document.getElementById('refreshInventory');

// Helper Functions
function showSpinner() {
    loadingSpinner.style.display = 'block';
}

function hideSpinner() {
    loadingSpinner.style.display = 'none';
}

function displayMessage(message, isSuccess = true) {
    orderMessage.style.color = isSuccess ? 'green' : 'red';
    orderMessage.textContent = message;
    setTimeout(() => orderMessage.textContent = '', 3000);
}

// Load Inventory Function
async function loadInventory() {
    showSpinner();
    inventoryList.innerHTML = '';

//     try {
//         const response = await fetch(`${API_BASE}inventory/`); // Correct use of template literal
//         if (response.ok) {
//             const inventory = await response.json();
//             inventory.forEach(item => {
//                 const li = document.createElement('li');
//                 li.textContent = `${item.product_name}: ${item.quantity} in stock`; // Correct use of template literal
//                 inventoryList.appendChild(li);
//             });
//         } else {
//             displayMessage('Error loading inventory.', false);
//         }
//     } catch (error) {
//         displayMessage('Failed to connect to server.', false);
//     } finally {
//         hideSpinner();
//     }
// }

try {
    const response = await fetch(`${API_BASE}inventory/products/`); // Updated API endpoint
    if (response.ok) {
        const inventory = await response.json(); // Parse JSON response
        inventory.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.product_name}: ${item.quantity} in stock`; // Format inventory item
            inventoryList.appendChild(li); // Append to the inventory list
        });
    } else {
        displayMessage('Error loading inventory.', false);
    }
} catch (error) {
    displayMessage('Failed to connect to server.', false);
} finally {
    hideSpinner(); // Hide the spinner once the loading process is done
}
}

// Handle Order Form Submission
orderForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const productName = productNameInput.value.trim();
    const quantity = parseInt(quantityInput.value, 10);

    if (!productName || quantity <= 0) {
        displayMessage('Invalid input. Please try again.', false);
        return;
    }

    showSpinner();

    try {
        const response = await fetch(`${API_BASE}orders/`, { // Correct use of template literal
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ product_name: productName, quantity }),
        });

        if (response.ok) {
            displayMessage('Order placed successfully!');
            loadInventory();
            orderForm.reset();
        } else {
            displayMessage('Error placing order. Try again.', false);
        }
    } catch (error) {
        displayMessage('Failed to connect to server.', false);
    } finally {
        hideSpinner();
    }
});

// Refresh Inventory Button
refreshButton.addEventListener('click', loadInventory);

// Initial Load
loadInventory();
