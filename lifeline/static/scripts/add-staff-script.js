function toggleSpecialistsField() {
    const dropdown = document.getElementById("dropdown");
    const specialistsField = document.getElementById("specialistsField");

    // If 'Doctor' is selected, show the specialists field, else hide it
    if (dropdown.value == "1") {
        specialistsField.style.display = "block"; // Show the field
    } else {
        specialistsField.style.display = "none"; // Hide the field
    }
}