from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch(executable_path="/usr/bin/google-chrome");pg=b.new_page(viewport={"width":1280,"height":800})
  for n in ["agent-dashboard","checklist","admin-review"]:
    pg.goto(f"file:///workspace/compliance-mockup/{n}.html");pg.screenshot(path=f"/workspace/compliance-mockup/{n}.png",full_page=True)
  b.close()
