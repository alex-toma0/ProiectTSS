import { test, expect } from "@playwright/test";
test("Upload", async ({ page }) => {
  const [name, email, password] = ["a2", "a2@a2.com", "a2"];
  const [songTitle, songImage, songGenre, songPath] = [
    "Underpass",
    "https://raw.githubusercontent.com/alex-toma0/images/main/pop-cover.jpg",
    "Pop",
    "test-files/Golden-Grey-Underpass.ogg",
  ];
  await page.goto("http://localhost:5173/login");
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Password").fill(password);

  // Click the login button
  await page.getByRole("button", { name: "Login" }).click();

  // Navigates to the profile page
  await page.getByRole("link", { name: "Profile" }).click();

  // Clicks the upload button
  await page
    .getByRole("button", {
      name: "Upload song",
    })
    .click();

  // Fills the form
  await page.getByLabel("Song Title").fill(songTitle);
  await page.getByLabel("Image Path").fill(songImage);
  await page.getByPlaceholder("Enter the genre").selectOption(songGenre);

  // Chooses the audio file
  const fileChooserPromise = page.waitForEvent("filechooser");
  await page.getByText("Choose song").click();
  const fileChooser = await fileChooserPromise;
  await fileChooser.setFiles(songPath);

  // Uploads the song
  await page.getByRole("button", { name: "Upload song" }).click();

  // Navigates to the profile page
  await page.getByRole("link", { name: "Profile" }).click();
  // Navigates to home page
  await page.getByRole("link", { name: "Streaming App" }).click();

  // Checks if the song was uploaded succesfully
  await expect(page.getByText(songTitle)).toBeVisible();
});
