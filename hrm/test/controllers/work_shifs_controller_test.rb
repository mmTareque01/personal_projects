require "test_helper"

class WorkShifsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @work_shif = work_shifs(:one)
  end

  test "should get index" do
    get work_shifs_url
    assert_response :success
  end

  test "should get new" do
    get new_work_shif_url
    assert_response :success
  end

  test "should create work_shif" do
    assert_difference("WorkShif.count") do
      post work_shifs_url, params: { work_shif: { from: @work_shif.from, name: @work_shif.name, to: @work_shif.to } }
    end

    assert_redirected_to work_shif_url(WorkShif.last)
  end

  test "should show work_shif" do
    get work_shif_url(@work_shif)
    assert_response :success
  end

  test "should get edit" do
    get edit_work_shif_url(@work_shif)
    assert_response :success
  end

  test "should update work_shif" do
    patch work_shif_url(@work_shif), params: { work_shif: { from: @work_shif.from, name: @work_shif.name, to: @work_shif.to } }
    assert_redirected_to work_shif_url(@work_shif)
  end

  test "should destroy work_shif" do
    assert_difference("WorkShif.count", -1) do
      delete work_shif_url(@work_shif)
    end

    assert_redirected_to work_shifs_url
  end
end
