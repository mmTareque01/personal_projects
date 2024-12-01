class LangagesController < ApplicationController
  before_action :set_langage, only: %i[ show edit update destroy ]

  # GET /langages or /langages.json
  def index
    @langages = Langage.all
  end

  # GET /langages/1 or /langages/1.json
  def show
  end

  # GET /langages/new
  def new
    @langage = Langage.new
  end

  # GET /langages/1/edit
  def edit
  end

  # POST /langages or /langages.json
  def create
    @langage = Langage.new(langage_params)

    respond_to do |format|
      if @langage.save
        format.html { redirect_to langage_url(@langage), notice: "Langage was successfully created." }
        format.json { render :show, status: :created, location: @langage }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @langage.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /langages/1 or /langages/1.json
  def update
    respond_to do |format|
      if @langage.update(langage_params)
        format.html { redirect_to langage_url(@langage), notice: "Langage was successfully updated." }
        format.json { render :show, status: :ok, location: @langage }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @langage.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /langages/1 or /langages/1.json
  def destroy
    @langage.destroy!

    respond_to do |format|
      format.html { redirect_to langages_url, notice: "Langage was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_langage
      @langage = Langage.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def langage_params
      params.require(:langage).permit(:name, :meta)
    end
end
