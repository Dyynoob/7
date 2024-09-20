<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['rom'])) {
    $rom = $_FILES['rom'];
    $allowedTypes = ['application/octet-stream']; // Adjust as needed
    if (in_array($rom['type'], $allowedTypes) && move_uploaded_file($rom['tmp_name'], 'roms/' . basename($rom['name']))) {
        echo "ROM uploaded successfully!";
    } else {
        echo "Upload failed. Ensure the file is a valid ROM.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload ROM</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Upload a ROM</h1>
    <form action="upload.php" method="POST" enctype="multipart/form-data">
        <label for="rom">Select ROM file:</label>
        <input type="file" name="rom" id="rom" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
