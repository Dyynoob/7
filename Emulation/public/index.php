<?php
$roms = array_diff(scandir('roms/'), ['.', '..']);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Play ROMs</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Select a ROM to Play</h1>
    <ul>
        <?php foreach ($roms as $rom): ?>
            <li><a href="play.php?rom=<?= urlencode($rom) ?>"><?= htmlspecialchars($rom) ?></a></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>

