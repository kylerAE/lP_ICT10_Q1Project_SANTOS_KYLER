import os
import webbrowser

products = [
    ("Pokémon Booster Pack", 250.00),
    ("Pokémon Elite Trainer Box", 2200.00),
    ("Special Edition Pokémon Card", 1200.00),
    ("Basketball Sneakers (Nike)", 6500.00),
    ("Basketball Sneakers (Adidas)", 5800.00),
]

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Kyler's Hobby Shop</title>
  <style>
    :root{--purple-1:#6b21a8;--purple-2:#9333ea;--bg:#f3f2f8;--card:#ffffff;--muted:#6b6b7a}
    html,body{height:100%;margin:0;padding:0;background:var(--bg);font-family: Arial, Helvetica, sans-serif;color:#222}
    .hero{background:linear-gradient(135deg,var(--purple-1),var(--purple-2));color:#fff;text-align:center;padding:36px 20px;border-radius:0 0 12px 12px;box-shadow:0 6px 18px rgba(0,0,0,0.12)}
    .hero h1{margin:0;font-size:2.6rem;letter-spacing:0.6px}
    .hero p{margin:6px 0;opacity:0.95}
    .wrap{width:80%;max-width:1100px;margin:28px auto}
    .card{background:var(--card);border-radius:12px;padding:18px;box-shadow:0 6px 20px rgba(17,17,17,0.06)}
    .menu-title{color:var(--purple-1);margin:0 0 12px 0;font-size:1.15rem;font-weight:600}
    table{width:100%;border-collapse:collapse}
    thead th{background:#fbf8ff;color:var(--purple-1);padding:14px 16px;text-align:left;font-weight:600;border-radius:6px}
    th,td{padding:14px 16px;border-bottom:1px solid #eee;font-size:1rem}
    td:last-child{text-align:right;font-weight:700}
    .footer-wrap{width:80%;max-width:1100px;margin:18px auto 46px auto;text-align:center}
    .hours{background:#fff;padding:16px;border-radius:10px;box-shadow:0 6px 18px rgba(0,0,0,0.06);color:var(--muted);margin-bottom:12px;font-style:italic}
    .cta{display:inline-block;background:linear-gradient(135deg,var(--purple-2),var(--purple-1));color:#fff;padding:8px 18px;border-radius:8px;text-decoration:none;font-weight:700}
    @media (max-width:900px){.hero h1{font-size:1.8rem}.wrap,.footer-wrap{width:94%}th,td{padding:12px}}
  </style>
</head>
<body>
  <header class="hero">
    <h1>Kyler's Hobby Shop</h1>
    <p>Owner: Kyler Santos • Based in Parañaque</p>
    <p>Since 2025</p>
  </header>

  <main class="wrap">
    <section class="card">
      <h2 class="menu-title">Product Pricelist</h2>
      <table>
        <thead>
          <tr><th>Product Name</th><th>Price (₱)</th></tr>
        </thead>
        <tbody>
"""

rows = ""
for name, price in products:
    rows += f"          <tr><td>{name}</td><td>₱{price:.2f}</td></tr>\n"

html_end = """        </tbody>
      </table>
    </section>
  </main>

  <div class="footer-wrap">
    <div class="hours">Open: 10:00 AM – 8:00 PM</div>
    <a class="cta" href="#">In-store Pickup Available</a>
  </div>
</body>
</html>
"""

content = html_start + rows + html_end

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

path = os.path.abspath("index.html")
webbrowser.open("file://" + path)
