import { test, expect } from "@playwright/test";
const [email, name, password] = ["test@test.com", "test", "test"];
test("Authentication Flow", async ({ page }) => {
  await page.goto("http://localhost:5173/register");
  // Fill the form
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Display Name").fill(password);
  await page.getByLabel("Password").fill(password);
  await page.getByPlaceholder("Confirm Password").fill(password);

  // Click the create account button
  await page.getByRole("button", { name: "Create account" }).click();

  // Checks if registration worked
  await page.waitForURL("http://localhost:5173/login");

  // Fill the form
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Password").fill(password);

  // Click the login button
  await page.getByRole("button", { name: "Login" }).click();
  // Checks if login was successful
  await expect(page.getByRole("button", { name: "Genre" })).toBeVisible();
});
