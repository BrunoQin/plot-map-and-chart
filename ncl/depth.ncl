load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
begin
f=addfile("2_9_origin.nc","r")    ;目标函数表现最好的粒子
g=addfile("ocean_temp_salt.res.nc","r")      ;原始文件
h=addfile("../output/00510101.ocean_month.nc","r")
;t1=f->temp(:,0:20,95:96,0:219)
;t2=g->temp(0:11,0:20,95:96,0:219)   ;0.5°南北纬平均
t1=f->temp(0,0:20,83:108,0:219)
t2=g->temp(0,0:20,83:108,0:219)    ;南北纬5°平均
del=t1-t2
printVarSummary(del)
t=h->temp(0,0:20,83:108,0:219)
copy_VarCoords(t,del)
delta=dim_avg_n_Wrap(del,1)
print(min(delta))
print(max(delta))
month_abbr = (/"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"/)
wks=gsn_open_wks("ps","depth")
gsn_define_colormap(wks,"BlueDarkRed18")
res=True
res@gsnDraw=False
res@gsnFrame=False
res@gsnAddCyclic=False
res@mpCenterLonF=180
;res@mpFillDrawOrder="PostDraw"
res@gsnSpreadColors=True
res@gsnSpreadColorEnd=-1
;res@cnLevelSelectionMode="ManualLevels"
;res@cnLevelSpacingF=2
;res@cnMinLevelValF=-12
;res@cnMaxLevelValF=12
res@pmTickMarkDisplayMode="Always"
res@lbLabelBarOn=False
;res@lbLabelAutoStride=True
res@cnLinesOn= False
;res@mpFillOn= False
res@cnLineLabelsOn=False
res@cnFillOn=True
res@tiYAxisOn=True
res@tiYAxisString="Depth"
res@tiYAxisFontHeightF=0.05     ;Y轴名称字体大小
res@trYReverse=True             ;把纵轴倒过来，深度从小到大
res@tmXBLabelFontHeightF=0.02    ;XY轴坐标标注字体大小
res@tmYLLabelFontHeightF=0.02
res@pmLegendDisplayMode="Never"
;res@cnLevelSelectionMode="ExplicitLevels"
;res@cnLevels=(/0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30/)
;res@cnFillColors=(/12,17,22,27,32,37,42,47,52,57,62,67,72,77,82,87,92/)
;画随深度扰动发展图的时候需要的脚本
;plots=new(12,graphic)
;do i=0,11
    ;res@gsnCenterString = month_abbr(i)
    ;res@gsnCenterStringFontHeightF=0.05      ;设定小图题目字体大小
    ;plots(i)=gsn_csm_contour(wks,delta(i,:,:),res)
;end do
;panel_res=True
;panel_res@gsnPanelLabelBar= True              ; add common colorbar
;panel_res@lbOrientation= "vertical"
;panel_res@pmLabelBarParallelPosF=0.50
;panel_res@pmLabelBarOrthogonalPosF=.50
;panel_res@gsnSpreadColors=True
;panel_res@gsnSpreadColorEnd=-1
;panel_res@cnLevelSelectionMode="ManualLevels"
;panel_res@cnLevelSpacingF=2
;panel_res@cnMinLevelValF=-12
;panel_res@cnMaxLevelValF=12
;wks1=gsn_open_wks("ps","pannel")
;gsn_panel(wks1, plots,(/3,4/),panel_res)
plot=gsn_csm_contour(wks,delta,res)
draw(plot)
frame(wks)
end
