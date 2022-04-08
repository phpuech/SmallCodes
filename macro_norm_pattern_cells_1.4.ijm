
// macro_norm_pattern    works on a stack ricm images with Fiji 32 bits
// outputs in resultats.txt    RadVar    IBavg    IBsd    ArInit  ArNorm    PerNorm    ArShr    ArTight    ICvar    ICinit    Slice
// for a range a variance radius
run("Clear Results");
roiManager("Reset");
IJ.log("\\Close");
run("Set Measurements...", "area mean standard min center perimeter bounding stack display redirect=None decimal=3");//réglage des informations que l'on veut
Dialog.create("Parametres");
Dialog.addString("Entrez le nom de la sequence RICM", "testR6.tif");            // nameRicm        //demande du nom de l'image ricm
Dialog.addNumber("Entrez la largeur du cadre(pixel)", 10);      // Lc
Dialog.addNumber("Entrez la valeur d'elargissement du ROI (pixel)", 10);        // Le
Dialog.addNumber("Entrez la valeur de l'aire min (pixel²)", 3000);          // Amin            //demande de l'aire minimale
Dialog.addNumber("Entrez la valeur de l'aire max (pixel²)", 1000000);            // Amax            //demande de l'aire maximale
Dialog.addNumber("Entrez la valeur de la circularite min", 0.2);          // Cmin            //demande de la circularite minimale
Dialog.addNumber("Entrez la valeur de la circularite max", 1);          // Cmax            //demande de la circularite maximale
Dialog.addNumber("Entrez la valeur du rayon de la variance init (pixel)", 6);        // Rv
//Dialog.addNumber("Entrez la valeur du rayon de la variance min (pixel)", 2);        // RvMin
//Dialog.addNumber("Entrez la valeur du rayon de la variance max (pixel)", 16);        // RvMax        Dialog.addCheckbox("Moyenne", true);                        // moyennage
//Dialog.addNumber("Entrez la valeur du seuil for normalized variance image", 0.02);    // LowerNorm
Dialog.addCheckbox("check ?", true);
Dialog.addCheckbox("Corner substraction", true);  // corner (dark) intensity substraction
Dialog.addNumber("Corner size (pixel)", 30);
Dialog.addNumber("Manual dark intensity", 300);      // DarkInt
Dialog.show();
nameRicm=Dialog.getString();
Lc=Dialog.getNumber();
Le=Dialog.getNumber();
Amin=Dialog.getNumber();
Amax=Dialog.getNumber();
Cmin=Dialog.getNumber();
Cmax=Dialog.getNumber();
Rv=Dialog.getNumber();
//RvMin=Dialog.getNumber();
//RvMax=Dialog.getNumber();
//lowerNorm=Dialog.getNumber();
check=Dialog.getCheckbox();
corner=Dialog.getCheckbox();
cornerSize=Dialog.getNumber();
DarkInt=Dialog.getNumber();
upperNorm=1; lowerNorm=0.04;
lowerTight=0; upperTight=0.8;
RvMin=2; RvMax=16;
selectWindow(nameRicm);
setSlice(1);
nS=nSlices;
getDimensions(width, height, channels, slices, frames); //waitForUser("Test");

setSlice(1);
for(i=0; i<nS; i++)
    {
    MeanB=DarkInt;
    if (corner==true)
    {
        makeRectangle(0, 0, cornerSize, cornerSize);
        setKeyDown("shift");
        makeRectangle(0, height-cornerSize, cornerSize, cornerSize); //makeRectangle(0, 952, 50, 50);
        setKeyDown("shift");
        makeRectangle(width-cornerSize, height-cornerSize, cornerSize, cornerSize); //makeRectangle(954, 952, 50, 50);
        setKeyDown("shift");
        makeRectangle(width-cornerSize, 0, cornerSize, cornerSize); //makeRectangle(954, 0, 50, 50);
        run("Measure");      //mesure dans les coins
        MeanB=getResult('Mean');
    }
    run("Select None");
    run("Subtract...", "value="+MeanB+" slice");//soustraction de la valeur moyenne d'intensite dans les coins
    run("Enhance Contrast", "saturated=0.35");
    if (i<nS-1){
        run("Next Slice [>]");    }
    }
setSlice(1);

repertoire=getDirectory("Repertoire de sauvegarde");
selectWindow(nameRicm);
setSlice(1);
run("Slice Keeper", "first=1 last="+nSlices+" increment=1");
run("Duplicate...", "title=["+nameRicm+" bis] duplicate range=1-"+nSlices);
selectWindow(nameRicm+" kept stack");
run("Close");
selectWindow(nameRicm+" bis");
run("Square Root", "stack");
run("Variance...", "radius="+Rv+" stack");
run("Threshold...");
waitForUser;
getThreshold(lower, upper);
run("Analyze Particles...", "size="+Amin+"-"+Amax+" circularity="+Cmin+"-"+Cmax+" show=Nothing add stack");  //detection des cellules
selectWindow(nameRicm+" bis");
run("Close");
nCells=roiManager("count");

for (i=0; i<nCells; i++)
    {
    roiManager("Show None");
    roiManager("Select", i);
    if (check==true)                                        //avec check
        {
        Dialog.create("OK ?");
        Dialog.addCheckbox("oui", true);
        Dialog.show();
        x= Dialog.getCheckbox();
        }
    else x=true;                                            //sans check
    if (x==false)
        {
        roiManager("Delete");
        i=i-1; nCells=nCells-1;
        }
    //mesure de chaque celulle
    }

roiManager("Save", repertoire+"RoiSet.zip");        // save chosen all cell rois

SliceO=newArray(nCells);
for (i=0; i<nCells; i++)
    {
    roiManager("Select", i);
    run("Measure");
    SliceO[i]=getResult('Slice');        // first slice of a given illumination
    }

slice=newArray(nCells);
IBavg=newArray(nCells);
ICinit=newArray(nCells);
ArInit=newArray(nCells);
ArNorm=newArray(nCells);
PerNorm=newArray(nCells);
ArShr=newArray(nCells);
ArTight=newArray(nCells);
ICvar=newArray(nCells);
nom=newArray(nCells);
IBsd=newArray(nCells);
res="RadVar    IBavg    IBsd    ArInit    ArNorm    PerNorm  ArShr    ArTight    ICvar    ICinit    Slice\n";
roiManager("Reset");
for (RadVar=RvMin; RadVar<=RvMax; RadVar++)
{
for (i=0; i<nCells; i++)    //loop on cells
    {
    selectWindow(nameRicm);
    setSlice(SliceO[i]);
    roiManager("Reset");
    roiManager("Open", repertoire+"RoiSet.zip");        // retrieve roi from stored zip file
    roiManager("Select", i);
    roiManager("Reset");
    roiManager("Add");
    run("Measure");
    ArInit[i]=getResult('Area');
    ICinit[i]=getResult('Mean');
    run("Enlarge...", "enlarge="+Le);        // enlarge original cell roi
    run("To Bounding Box");                    // find smallest rectangle containing enlarged cell roi
    run("Enlarge...", "enlarge="+Lc+" pixel");        // enlarge rectangle
    roiManager("Add");
    roiManager("Select All");
    roiManager("XOR");                    // define "frame" as enlarged rectangle minus enlarged cell roi
    roiManager("Reset");
    roiManager("Add");
    run("Measure");
    IBavg[i]=getResult('Mean');            //mesure de l'intensite du background originale from frame
    IBsd[i]=getResult('StdDev');
    run("Slice Keeper", "first="+(SliceO[i])+" last="+(SliceO[i])+" increment=1");
    roiManager("Select", 0);
                                // define small image containg frame ROI
    run("Scale...", "x=1.0 y=1.0 z=1.0 depth="+nSlices+" interpolation=None create title=Cell-"+i);
    roiManager("Select", 0);
    setSelectionLocation(0,0);                // displace frame ROI into small image
    roiManager('update');
    roiManager("Select", 0);
    selectWindow("Cell-"+i);
    run("Nonuniform Background Removal", "surface=[Fit Cubic Surface] show");   //plugin correction du fond avec affichage
//    run("Nonuniform Background Removal", "surface=[Fit Cubic Surface]");   //plugin correction du fond sans affichage
    run("Close");
    roiManager("Reset");
    imageCalculator("Divide create 32-bit", "Cell-"+i,"Cell-"+i+" - Cubic Polynomial Background");
    selectWindow("Result of Cell-"+i);
    run("Duplicate...", "title=Cell-"+i+"norm");

    run("Threshold...");
    setThreshold(lowerTight, upperTight);
    run("Analyze Particles...", "size=10-"+Amax+" circularity=0.01-"+Cmax+" show=Nothing add");
    roiManager("Select All");
    roiManager("Combine");
    roiManager("Reset");
    roiManager("Add");
    roiManager("Save", repertoire+"RoiSet1.zip");
    run("Measure");
    ArTight[i]=getResult('Area');
    roiManager("Reset");
    selectWindow("Result of Cell-"+i);
    run("Variance...", "radius="+(RadVar));
    run("Square Root");
    run("Threshold...");
    setThreshold(lowerNorm, upperNorm);
    run("Analyze Particles...", "size="+(Amin/10)+"-"+Amax+" circularity="+(Cmin/10)+"-"+Cmax+" show=Nothing add");
//    run("Analyze Particles...", "size="+Amin+"-"+Amax+" circularity="+Cmin+"-"+Cmax+" show=Nothing add");
//    roiManager("Select All");
    n = roiManager("count");
    if (n>0){
        roiManager("Select", 0);
        run("Measure");
        ArNorm[i]=getResult('Area');
        PerNorm[i]=getResult('Perim.');
        run("Enlarge...", "enlarge=-"+RadVar);        // shrinks original cell roi
        roiManager("Add");
        roiManager("Save", repertoire+"RoiSet2.zip");
        run("Measure");
        ICvar[i]=getResult('Mean');
        ArShr[i]=getResult('Area');    }
    else {
        ArNorm[i]=0; PerNorm[i]=0; ICvar[i]=0; ArShr[i]=0;}
    selectWindow(nameRicm+" kept stack");
    run("Close");
    selectWindow("Cell-"+i+" - Cubic Polynomial Background");
    close();
    selectWindow("Cell-"+i);
    close();
    selectWindow("Result of Cell-"+i);
    close();
    selectWindow("Cell-"+i+"norm");
    close();
    }


for (i=0; i<nCells; i++)
    {
    res=res+RadVar+"    "+IBavg[i]+"    "+IBsd[i]+"  "+ArInit[i]+"    "+ArNorm[i]+"    "+PerNorm[i]+"    "+ArShr[i]+"  "+ArTight[i]+"    "+ICvar[i]+"    "+ICinit[i]+"  "+SliceO[i]+"\n";
    }
}    // end loop on RadVar
IJ.log(res);
wait(100);
saveAs("text", repertoire+"resultats.txt");


