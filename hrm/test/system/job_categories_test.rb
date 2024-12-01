require "application_system_test_case"

class JobCategoriesTest < ApplicationSystemTestCase
  setup do
    @job_category = job_categories(:one)
  end

  test "visiting the index" do
    visit job_categories_url
    assert_selector "h1", text: "Job categories"
  end

  test "should create job category" do
    visit job_categories_url
    click_on "New job category"

    fill_in "Meta", with: @job_category.meta
    fill_in "Name", with: @job_category.name
    click_on "Create Job category"

    assert_text "Job category was successfully created"
    click_on "Back"
  end

  test "should update Job category" do
    visit job_category_url(@job_category)
    click_on "Edit this job category", match: :first

    fill_in "Meta", with: @job_category.meta
    fill_in "Name", with: @job_category.name
    click_on "Update Job category"

    assert_text "Job category was successfully updated"
    click_on "Back"
  end

  test "should destroy Job category" do
    visit job_category_url(@job_category)
    click_on "Destroy this job category", match: :first

    assert_text "Job category was successfully destroyed"
  end
end
