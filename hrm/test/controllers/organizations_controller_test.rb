require "test_helper"

class OrganizationsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @organization = organizations(:one)
  end

  test "should get index" do
    get organizations_url
    assert_response :success
  end

  test "should get new" do
    get new_organization_url
    assert_response :success
  end

  test "should create organization" do
    assert_difference("Organization.count") do
      post organizations_url, params: { organization: { address_street_1: @organization.address_street_1, address_street_2: @organization.address_street_2, city: @organization.city, country: @organization.country, email: @organization.email, employee: @organization.employee, name: @organization.name, phone: @organization.phone, postal_code: @organization.postal_code, reg_no: @organization.reg_no, state: @organization.state, tex_id: @organization.tex_id } }
    end

    assert_redirected_to organization_url(Organization.last)
  end

  test "should show organization" do
    get organization_url(@organization)
    assert_response :success
  end

  test "should get edit" do
    get edit_organization_url(@organization)
    assert_response :success
  end

  test "should update organization" do
    patch organization_url(@organization), params: { organization: { address_street_1: @organization.address_street_1, address_street_2: @organization.address_street_2, city: @organization.city, country: @organization.country, email: @organization.email, employee: @organization.employee, name: @organization.name, phone: @organization.phone, postal_code: @organization.postal_code, reg_no: @organization.reg_no, state: @organization.state, tex_id: @organization.tex_id } }
    assert_redirected_to organization_url(@organization)
  end

  test "should destroy organization" do
    assert_difference("Organization.count", -1) do
      delete organization_url(@organization)
    end

    assert_redirected_to organizations_url
  end
end
