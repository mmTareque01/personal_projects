require "application_system_test_case"

class WorkShifsTest < ApplicationSystemTestCase
  setup do
    @work_shif = work_shifs(:one)
  end

  test "visiting the index" do
    visit work_shifs_url
    assert_selector "h1", text: "Work shifs"
  end

  test "should create work shif" do
    visit work_shifs_url
    click_on "New work shif"

    fill_in "From", with: @work_shif.from
    fill_in "Name", with: @work_shif.name
    fill_in "To", with: @work_shif.to
    click_on "Create Work shif"

    assert_text "Work shif was successfully created"
    click_on "Back"
  end

  test "should update Work shif" do
    visit work_shif_url(@work_shif)
    click_on "Edit this work shif", match: :first

    fill_in "From", with: @work_shif.from
    fill_in "Name", with: @work_shif.name
    fill_in "To", with: @work_shif.to
    click_on "Update Work shif"

    assert_text "Work shif was successfully updated"
    click_on "Back"
  end

  test "should destroy Work shif" do
    visit work_shif_url(@work_shif)
    click_on "Destroy this work shif", match: :first

    assert_text "Work shif was successfully destroyed"
  end
end
