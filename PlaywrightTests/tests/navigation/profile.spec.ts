import { test, expect } from "@playwright/test";
test("Profile Navigation", async ({ page }) => {
  const [name, email, password] = ["a2", "a2@a2.com", "a2"];
  await page.goto("http://localhost:5173/login");
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Password").fill(password);

  // Click the login button
  await page.getByRole("button", { name: "Login" }).click();

  // Navigates to the profile page
  await page.getByRole("link", { name: "Profile" }).click();

  // Checks if the elements of the profile loaded correctly
  await expect(page.getByRole("img")).toBeVisible();
  await expect(page.getByText(name)).toBeVisible();
  await expect(
    page.getByRole("button", {
      name: "Upload song",
    })
  ).toBeVisible();
  await expect(page.getByText("number of songs")).toBeVisible();
});
