from inventory.products import PRODUCTS


def create_main_page():

    product_items = "".join(
        f"<li><strong>{p['name']}</strong> - ${p['price']}<br><em>{p.get('description','')}</em></li>"
        for p in PRODUCTS
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>RoboStore</title>
      <link rel="icon" type="image/png" href="https://w7.pngwing.com/pngs/381/791/png-transparent-robowar-robot-human-head-face-robot-electronics-face-logo-thumbnail.png">

      <link rel="stylesheet" href="/web_page/style.css">
    </head>
    <body>
      <h1>Bienvenido a RoboStore</h1>
      <p>Productos disponibles:</p>
      <ul>
        {product_items}
      </ul>
    </body>
    </html>
    """
    return html
