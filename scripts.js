const API_BASE = 'http://127.0.0.1:8000/';

document.getElementById('orderForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const productName = document.getElementById('productName').value;
    const quantity = document.getElementById('quantity').value;

    const response = await fetch(`${API_BASE}/orders/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_name: productName, quantity: parseInt(quantity, 10) }),
    });

    if (response.ok) {
        alert('Order placed successfully!');
        loadInventory();
    } else {
        alert('Error placing order.');
    }
});

async function loadInventory() {
    const response = await fetch(`${API_BASE}/inventory/`);
    const inventoryList = document.getElementById('inventoryList');
    inventoryList.innerHTML = '';

    if (response.ok) {
        const inventory = await response.json();
        inventory.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.product_name}: ${item.quantity} in stock`;
            inventoryList.appendChild(li);
        });
    }
}

loadInventory();
