require "application_system_test_case"

class NationalitiesTest < ApplicationSystemTestCase
  setup do
    @nationality = nationalities(:one)
  end

  test "visiting the index" do
    visit nationalities_url
    assert_selector "h1", text: "Nationalities"
  end

  test "should create nationality" do
    visit nationalities_url
    click_on "New nationality"

    fill_in "Country", with: @nationality.country
    fill_in "Name", with: @nationality.name
    click_on "Create Nationality"

    assert_text "Nationality was successfully created"
    click_on "Back"
  end

  test "should update Nationality" do
    visit nationality_url(@nationality)
    click_on "Edit this nationality", match: :first

    fill_in "Country", with: @nationality.country
    fill_in "Name", with: @nationality.name
    click_on "Update Nationality"

    assert_text "Nationality was successfully updated"
    click_on "Back"
  end

  test "should destroy Nationality" do
    visit nationality_url(@nationality)
    click_on "Destroy this nationality", match: :first

    assert_text "Nationality was successfully destroyed"
  end
end
