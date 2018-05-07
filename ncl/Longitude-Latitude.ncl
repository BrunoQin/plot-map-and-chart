begin
    swarm=addfile("../3_29_ocean.nc", "r")    ;目标函数表现最好的粒子
    origin=addfile("/BIGDATA1/iocas_mmu_2/GFDL-CM2p1/output/00610101.ocean_month.nc", "r")      ;原始文件

    ts = swarm->sst(0, :, :)
    ts@units = "degC"
    to = origin->sst(24, :, :)
    to@units = "degC"

    ts = ts - to

    ; t@lat2d = delta->lat2d
    ; t@lon2d = delta->lon2d

    wks = gsn_open_wks("png", "contour4d")    ; Open png file called "contour4d.png"

    res                 = True
    res@gsnAddCyclic    = True               ; Add cyclic point.
    res@cnFillOn        = True               ; Turn on contour fill.
    res@cnFillMode      = "RasterFill"       ; Turn on raster fill.

    ; res@gsnDraw             = False
    ; res@gsnFrame            = False
    ; res@mpFillOn            = False            ; no need
    res@mpCenterLonF        = -180.0

    res@cnLevelSelectionMode= "ManualLevels"   ; manual set levels
    res@cnMinLevelValF      = -3.0
    res@cnMaxLevelValF      = 3.0
    res@cnLevelSpacingF     = 0.3              ; 20 contour levels
    res@cnLinesOn           = False
    res@cnLineLabelsOn      = False
    res@cnInfoLabelOn       = False
    res@cnFillPalette       = "BlueDarkRed18"

    ; res@lbLabelBarOn        = False            ; turn off individual label bars

    res@gsnStringFontHeightF= 0.02
    res@gsnLeftString       = "SST"
    res@gsnRightString      = ts@units

    plot = gsn_csm_contour_map(wks, ts, res)    ; Call the gsn_csm function for
                                           ; drawing contours over a map.

end
