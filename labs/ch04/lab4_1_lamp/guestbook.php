<?php
// 实验 4-1：最简单的留言板，演示“网页（Apache + PHP）+ 数据库（MySQL / MariaDB）”的网站结构
$db = new mysqli("localhost", "webuser", "Web@2026", "guestbook");
$db->set_charset("utf8mb4");
if ($_SERVER["REQUEST_METHOD"] === "POST" && trim($_POST["msg"] ?? "") !== "") {
    $stmt = $db->prepare("INSERT INTO messages (name, msg) VALUES (?, ?)");
    $stmt->bind_param("ss", $_POST["name"], $_POST["msg"]);
    $stmt->execute();
}
$rows = $db->query("SELECT name, msg, created FROM messages ORDER BY id DESC LIMIT 20");
?>
<!doctype html>
<meta charset="utf-8">
<title>云上留言板</title>
<h1>云上留言板</h1>
<p>本页面运行在服务器 <b><?= gethostname() ?></b> 上，留言保存在 MySQL 数据库中。</p>
<form method="post">
  <input name="name" placeholder="你的名字" required>
  <input name="msg" placeholder="说点什么" size="40" required>
  <button>提交</button>
</form>
<ul>
<?php while ($r = $rows->fetch_assoc()): ?>
  <li><b><?= htmlspecialchars($r["name"]) ?></b>：<?= htmlspecialchars($r["msg"]) ?>（<?= $r["created"] ?>）</li>
<?php endwhile; ?>
</ul>
