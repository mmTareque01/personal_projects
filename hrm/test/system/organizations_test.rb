require "application_system_test_case"

class OrganizationsTest < ApplicationSystemTestCase
  setup do
    @organization = organizations(:one)
  end

  test "visiting the index" do
    visit organizations_url
    assert_selector "h1", text: "Organizations"
  end

  test "should create organization" do
    visit organizations_url
    click_on "New organization"

    fill_in "Address street 1", with: @organization.address_street_1
    fill_in "Address street 2", with: @organization.address_street_2
    fill_in "City", with: @organization.city
    fill_in "Country", with: @organization.country
    fill_in "Email", with: @organization.email
    fill_in "Employee", with: @organization.employee
    fill_in "Name", with: @organization.name
    fill_in "Phone", with: @organization.phone
    fill_in "Postal code", with: @organization.postal_code
    fill_in "Reg no", with: @organization.reg_no
    fill_in "State", with: @organization.state
    fill_in "Tex", with: @organization.tex_id
    click_on "Create Organization"

    assert_text "Organization was successfully created"
    click_on "Back"
  end

  test "should update Organization" do
    visit organization_url(@organization)
    click_on "Edit this organization", match: :first

    fill_in "Address street 1", with: @organization.address_street_1
    fill_in "Address street 2", with: @organization.address_street_2
    fill_in "City", with: @organization.city
    fill_in "Country", with: @organization.country
    fill_in "Email", with: @organization.email
    fill_in "Employee", with: @organization.employee
    fill_in "Name", with: @organization.name
    fill_in "Phone", with: @organization.phone
    fill_in "Postal code", with: @organization.postal_code
    fill_in "Reg no", with: @organization.reg_no
    fill_in "State", with: @organization.state
    fill_in "Tex", with: @organization.tex_id
    click_on "Update Organization"

    assert_text "Organization was successfully updated"
    click_on "Back"
  end

  test "should destroy Organization" do
    visit organization_url(@organization)
    click_on "Destroy this organization", match: :first

    assert_text "Organization was successfully destroyed"
  end
end
