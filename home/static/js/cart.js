// cart.js

function removeItem(courseId) {
    console.log("Removing item with courseId:", courseId);
    $.ajax({
        url: `/remove_from_cart/${courseId}/`,
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken  // Use a variable for the CSRF token
        },
        success: function() {
            console.log("Item removed successfully");
            location.reload();  // Reload to reflect changes
        },
        error: function(xhr, status, error) {
            console.error("Error removing item:", error);
        }
    });
}

function updateQuantity(courseId, increment) {
    console.log("Updating quantity for courseId:", courseId, "with increment:", increment);
    $.ajax({
        url: `/update_cart/${courseId}/${increment}/`,
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken  // Use a variable for the CSRF token
        },
        success: function() {
            console.log("Quantity updated successfully");
            location.reload();
        },
        error: function(xhr, status, error) {
            console.error("Error updating quantity:", error);
        }
    });
}

// CSRF token fetching function
function getCSRFToken() {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.substring(10);  // Return the CSRF token value
        }
    }
    return '';  // Return empty string if not found
}

// Initialize CSRF token
var csrftoken = getCSRFToken();  // Get CSRF token from cookies
