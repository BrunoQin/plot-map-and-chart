;----------------------------------------------------------------------
; panel_33.ncl
;
; Concepts illustrated:
;   - Combining two sets of paneled plots on one page
;   - Maximizing paneled plots after they've been created
;   - Drawing two labelbars in a combined panel plot
;----------------------------------------------------------------------
;
; These files are loaded by default in NCL V6.2.0 and newer
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin
;---Open file
    fname = "../1_16_ocean.nc"
    f     = addfile(fname, "r")
    fname_ave = "/BIGDATA1/iocas_mmu_2/GFDL-CM2p1/output/00610101.ocean_month.nc"
    f_ave     = addfile(fname_ave, "r")

    month_abbr = (/"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"/)

;---Read in temperature and convert to degrees C.
    t       = f->temp  ;南北纬5°平均
    t@units = "degC"
    t_ave   = f_ave->temp  ;南北纬5°平均
    t_ave@units = "degC"

;---Start the graphics
    wks  = gsn_open_wks("png","panel8")         ; send graphics to PNG file

    res                     = True
    res@gsnDraw             = False
    res@gsnFrame            = False
    res@gsnAddCyclic        = False
    ; res@mpCenterLonF        = 180.0

    res@cnLevelSelectionMode= "ManualLevels"   ; manual set levels
    res@cnMinLevelValF      = -4.0
    res@cnMaxLevelValF      = 4.0
    res@cnLevelSpacingF     = 0.4              ; 20 contour levels
    res@cnFillOn            = True             ; color fill plot
    res@cnLinesOn           = False
    res@cnLineLabelsOn      = False
    res@cnInfoLabelOn       = False
    res@cnFillPalette       = "BlueDarkRed18"

    res@tiYAxisOn           = True
    res@tiYAxisString       = "Depth"
    res@tiYAxisFontHeightF  = 0.02             ;Y轴名称字体大小
    res@trYReverse          = True             ;把纵轴倒过来，深度从小到大
    res@tmXBLabelFontHeightF= 0.02    ;XY轴坐标标注字体大小
    res@tmYLLabelFontHeightF= 0.02

    res@lbLabelBarOn        = False            ; turn off individual label bars

    res@gsnStringFontHeightF= 0.02
    ; res@gsnLeftString       = "Depth"
    ; res@gsnRightString      = t@units
    res@pmLegendDisplayMode = "Never"

;---Create arrays to hold series of plots
    plots      = new(12, graphic)

;---Get data for start and end year of interest
    del = t(:, 0:11, 83:108, 39:201) - t_ave(24:35, 0:11, 83:108, 39:201)
    copy_VarCoords(t, del)
    delta = dim_avg_n_Wrap(del, 2)

    do i=0, 11

;---Create plot
     res@gsnCenterString = month_abbr(i)
     res@gsnCenterStringFontHeightF=0.01      ;设定小图题目字体大小

     plots(i)=gsn_csm_contour(wks, delta(i, :, :), res)

    end do

;---Resources for paneling
    pres                   = True              ; modify the panel plot
    pres@gsnPanelMainString= fname
    pres@gsnFrame          = False             ; don't advance frame yet
    pres@gsnDraw           = False             ; draw later, in maximize mode
    pres@gsnPanelBottom    = 0.33              ; top 2/3 of frame

    pres@gsnPanelLabelBar  = True              ; add common colorbar
    pres@lbOrientation     = "vertical"
    pres@pmLabelBarWidthF  = 0.075             ; make thinner
    pres@pmLabelBarHeightF = 0.40

;
; It is necessary to return the id of the paneled plots,
; so they can "live" for the rest of this script, for
; when we maximize them later.
;
    panelid1 = gsn_panel_return(wks, plots, (/3,4/), pres)

;---Calculate location for top of difference plots
    bb     = NhlGetBB(panelid1)
    bottom = min(bb(:,1))
    top    = max(bb(:,0))
    height = (top-bottom)/2.     ; Height of one row

;---Panel the diff plots at the bottom
;    delete(pres@gsnPanelMainString)
;    pres@gsnPanelTop       = bottom-0.01    ; lower 1/3 plus some white space
;    pres@gsnPanelBottom    = pres@gsnPanelTop - height

;    pres@pmLabelBarHeightF = 0.20

;    panelid2 = gsn_panel_return(wks,diff_plots,(/1,2/),pres)

;---This will maximize the size of all the paneled stuff.
    maximize_output(wks,True)
end
