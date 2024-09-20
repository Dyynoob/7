<?php
if (!isset($_GET['rom'])) {
    die("No ROM selected.");
}

$rom = urldecode($_GET['rom']);
$romPath = 'roms/' . basename($rom);

if (!file_exists($romPath)) {
    die("ROM file does not exist.");
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Playing <?= htmlspecialchars($rom) ?></title>
    <script src="emulator/emulator.js"></script>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Playing: <?= htmlspecialchars($rom) ?></h1>
    <div id="emulator"></div>

    <script>
        var emulator = new Emulator(document.getElementById('emulator'));
        emulator.loadRom('<?= htmlspecialchars($romPath) ?>');
    </script>
</body>
</html>
