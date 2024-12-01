require "application_system_test_case"

class LangagesTest < ApplicationSystemTestCase
  setup do
    @langage = langages(:one)
  end

  test "visiting the index" do
    visit langages_url
    assert_selector "h1", text: "Langages"
  end

  test "should create langage" do
    visit langages_url
    click_on "New langage"

    fill_in "Meta", with: @langage.meta
    fill_in "Name", with: @langage.name
    click_on "Create Langage"

    assert_text "Langage was successfully created"
    click_on "Back"
  end

  test "should update Langage" do
    visit langage_url(@langage)
    click_on "Edit this langage", match: :first

    fill_in "Meta", with: @langage.meta
    fill_in "Name", with: @langage.name
    click_on "Update Langage"

    assert_text "Langage was successfully updated"
    click_on "Back"
  end

  test "should destroy Langage" do
    visit langage_url(@langage)
    click_on "Destroy this langage", match: :first

    assert_text "Langage was successfully destroyed"
  end
end
