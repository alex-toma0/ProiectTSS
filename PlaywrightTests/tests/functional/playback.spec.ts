import { test, expect } from "@playwright/test";
const [email, password] = ["a@a.com", "a"];
test("Playback", async ({ page }) => {
  await page.goto("http://localhost:5173/login");

  // Fill the form
  await page.getByLabel("Email address").fill(email);
  await page.getByLabel("Password").fill(password);

  // Click the login button
  await page.getByRole("button", { name: "Login" }).click();

  // Gets the first song title
  const song = page.locator(".card-body .card-title.h5").first();
  const title = await song.innerText();

  // Clicks the first play button
  await page.getByRole("button", { name: "Play" }).first().click();

  // Checks if the song has been queued in the player by comparing the titles
  const currentSong = page.locator(".interface-grid .title");
  const currentSongTitle = await currentSong.innerText();

  await expect(currentSongTitle === title).toBeTruthy();
});
