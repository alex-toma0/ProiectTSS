import { test, expect } from "@playwright/test";
const [email, password] = ["a@a.com", "a"];
test("Login", async ({ page }) => {
  await page.goto("http://localhost:5173/login");

  // Fill the form
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Password").fill(password);

  // Click the login button
  await page.getByRole("button", { name: "Login" }).click();

  // Checks if login was successful
  await expect(page.getByRole("button", { name: "Genre" })).toBeVisible();
});
