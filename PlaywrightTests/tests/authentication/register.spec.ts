import { test, expect } from "@playwright/test";
const [email, name, password] = ["aasdadsd@aaxxsas.com", "mjnas", "a"];
test("Register", async ({ page }) => {
  await page.goto("http://localhost:5173/register");

  // Fill the form
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Display Name").fill(name);
  await page.getByLabel("Password").fill(password);
  await page.getByPlaceholder("Confirm Password").fill(password);

  // Click the create account button
  await page.getByRole("button", { name: "Create account" }).click();

  // Checks if registration worked
  await page.waitForURL("http://localhost:5173/login");
  await expect(page.getByRole("button", { name: "Login" })).toBeVisible();
});
