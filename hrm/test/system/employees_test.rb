require "application_system_test_case"

class EmployeesTest < ApplicationSystemTestCase
  setup do
    @employee = employees(:one)
  end

  test "visiting the index" do
    visit employees_url
    assert_selector "h1", text: "Employees"
  end

  test "should create employee" do
    visit employees_url
    click_on "New employee"

    fill_in "Dob", with: @employee.dob
    fill_in "E", with: @employee.e_id
    fill_in "F name", with: @employee.f_name
    fill_in "Gender", with: @employee.gender
    fill_in "L name", with: @employee.l_name
    fill_in "Marital status", with: @employee.marital_status
    fill_in "N name", with: @employee.n_name
    fill_in "Nationality", with: @employee.nationality_id
    check "Smoker" if @employee.smoker
    click_on "Create Employee"

    assert_text "Employee was successfully created"
    click_on "Back"
  end

  test "should update Employee" do
    visit employee_url(@employee)
    click_on "Edit this employee", match: :first

    fill_in "Dob", with: @employee.dob
    fill_in "E", with: @employee.e_id
    fill_in "F name", with: @employee.f_name
    fill_in "Gender", with: @employee.gender
    fill_in "L name", with: @employee.l_name
    fill_in "Marital status", with: @employee.marital_status
    fill_in "N name", with: @employee.n_name
    fill_in "Nationality", with: @employee.nationality_id
    check "Smoker" if @employee.smoker
    click_on "Update Employee"

    assert_text "Employee was successfully updated"
    click_on "Back"
  end

  test "should destroy Employee" do
    visit employee_url(@employee)
    click_on "Destroy this employee", match: :first

    assert_text "Employee was successfully destroyed"
  end
end
