import { test, expect } from "@playwright/test";
test("Home Navigation", async ({ page }) => {
  const [email, password] = ["a2@a2.com", "a2"];

  // Logs in
  await page.goto("http://localhost:5173/login");
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Password").fill(password);
  // Click the login button
  await page.getByRole("button", { name: "Login" }).click();
  // Checks if navigating to the Home page works as expected
  await page.getByRole("link", { name: "Streaming App" }).click();
  await expect(
    page.getByRole("button", {
      name: "Genre",
    })
  ).toBeVisible();
});
