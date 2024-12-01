require "test_helper"

class LangagesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @langage = langages(:one)
  end

  test "should get index" do
    get langages_url
    assert_response :success
  end

  test "should get new" do
    get new_langage_url
    assert_response :success
  end

  test "should create langage" do
    assert_difference("Langage.count") do
      post langages_url, params: { langage: { meta: @langage.meta, name: @langage.name } }
    end

    assert_redirected_to langage_url(Langage.last)
  end

  test "should show langage" do
    get langage_url(@langage)
    assert_response :success
  end

  test "should get edit" do
    get edit_langage_url(@langage)
    assert_response :success
  end

  test "should update langage" do
    patch langage_url(@langage), params: { langage: { meta: @langage.meta, name: @langage.name } }
    assert_redirected_to langage_url(@langage)
  end

  test "should destroy langage" do
    assert_difference("Langage.count", -1) do
      delete langage_url(@langage)
    end

    assert_redirected_to langages_url
  end
end
