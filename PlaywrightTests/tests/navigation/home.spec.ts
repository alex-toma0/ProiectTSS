import { test, expect } from "@playwright/test";
test("Home Navigation", async ({ page }) => {
  // Checks if navigating to the Home page works as expected
  await page.goto("http://localhost:5173/");
  await page
    .getByRole("link", {
      name: "Streaming App",
    })
    .click();
  await page.waitForURL("http://localhost:5173/");
  await expect(
    page.getByRole("button", {
      name: "Genre",
    })
  ).toBeVisible();
});
