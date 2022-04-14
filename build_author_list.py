from string import ascii_lowercase
import datetime
import time
import os

thisTime = datetime.datetime.now()
generation_time = "Author list generated at {0:02d}:{1:02d}:{2:02d} {3} on {4} {5:02d}/{6:02d}/{7}".format(thisTime.hour
																										  ,thisTime.minute
																										  ,thisTime.second
																										  ,time.tzname[0]
																										  ,thisTime.strftime("%A")
																										  ,thisTime.day
																										  ,thisTime.month
																										  ,thisTime.year)

institute_list = []
association_list = []
author_list = []

institute_list.append(("AANL", "A. Alikhanyan National Laboratory, Yerevan, Armenia"))
institute_list.append(("AcademiaSinica", "Institute of Physics, Academia Sinica, Taipei, Taiwan"))
institute_list.append(("AUGIE", "Augustana University, Sioux Falls, SD, USA"))
institute_list.append(("BGU", "Ben-Gurion University of the Negev, Beersheba, Israel"))
institute_list.append(("BNL", "Brookhaven National Laboratory, Upton, NY, USA"))
institute_list.append(("BrunelUniversity", "Brunel University London, Uxbridge, UK"))
institute_list.append(("CanisiusCollege", "Canisius College, Buffalo, NY, USA"))
institute_list.append(("CCNU", "Central China Normal University, Wuhan, China"))
institute_list.append(("Charles", "Charles University, Faculty of Maths and Physics, Prague, Czech Republic"))
institute_list.append(("CIAE", "China Institute of Atomic Energy, Fangshan, Beijing, China"))
institute_list.append(("CNU", "Christopher Newport University, Newport News, VA, USA"))
institute_list.append(("Columbia", "Department of Physics, Columbia University, New York, NY, USA"))
institute_list.append(("CUA", "The Catholic University of America, Washington, DC, USA"))
institute_list.append(("CzechTechUniv", "Czech Technical University in Prague, Faculty of Nuclear Sciences and Physical Engineering, Czech Republic"))
institute_list.append(("Duquesne", "Duquesne University, Pittsburgh, PA, USA"))
institute_list.append(("Duke", "Duke University, Durham, NC, USA"))
institute_list.append(("FIU", "Florida International University, Miami, FL, USA"))
institute_list.append(("GeorgiaState", "Georgia State University, Atlanta, GA, USA"))
institute_list.append(("Glasgow", "School of Physics and Astronomy, University of Glasgow, Glasgow, UK"))
institute_list.append(("GSI", "GSI Helmholtzzentrum fuer Schwerionenforschung, Darmstadt, Germany"))
institute_list.append(("GWU", "The George Washington University, Washington, DC, USA"))
institute_list.append(("Hampton", "Hampton University, Hampton, VA, USA"))
institute_list.append(("HEAROKEK", "High Energy Accelerator Research Organization, Tsukuba, Japan"))
institute_list.append(("HUJI", "Racah Institute of Physics, Hebrew University, Jerusalem, Israel"))
institute_list.append(("IJCLabOrsay", "Universit\\'{{e}} Paris-Saclay, CNRS/IN2P3, IJCLab, Orsay, France"))
institute_list.append(("IMP", "Institute of Modern Physics, Chinese Academy of Sciences, Lanzhou, Gansu, China"))
institute_list.append(("Inha", "Inha University, Incheon, Republic of Korea"))
institute_list.append(("IowaState", "Iowa State University, Ames, IA, USA"))
institute_list.append(("IPAS", ""))
institute_list.append(("JAEA", ""))
institute_list.append(("JazanUniversity", "Jazan University, Jazan, Saudi Arabia"))
institute_list.append(("JeonbukNational", "Division of Science Education, Jeonbuk National University, Jeonju, Republic of Korea"))
institute_list.append(("JLab", "Thomas Jefferson National Accelerator Facility, Newport News, VA, USA"))
institute_list.append(("JMU", ""))
institute_list.append(("KobeUniversity", "Graduate School of Science, Kobe University, Kobe, Japan"))
institute_list.append(("KoreaUniversity", "Korea University, Seoul, Republic of Korea"))
institute_list.append(("Kyungpook", "Kyungpook National University, Daegu, Republic of Korea"))
institute_list.append(("LANL", "Los Alamos National Laboratory, Los Alamos, NM, USA"))
institute_list.append(("LBNL", "Lawrence Berkeley National Laboratory, Berkeley, CA, USA"))
institute_list.append(("LehighUniversity", "Lehigh University, Bethlehem, PA, USA"))
institute_list.append(("LLNL", "Lawrence Livermore National Laboratory, Livermore, CA, USA"))
institute_list.append(("MoreheadState", "Morehead State University, Morehad, KY, USA"))
institute_list.append(("MIT", "Massachusetts Institute of Technology, Cambridge, MA, USA"))
institute_list.append(("MSU", "Mississippi State University, Mississippi State, MS, USA"))
institute_list.append(("NCKU", "National Cheng Kung University, Tainan, Taiwan"))
institute_list.append(("NCU", "National Central University, Chungli, Taiwan"))
institute_list.append(("Nihon", "Nihon University, CST, Tokyo, Japan"))
institute_list.append(("NMSU", "New Mexico State University, Las Cruces, NM, USA"))
institute_list.append(("NRNUMEPhI", "National Research Nuclear University MEPhI, Moscow, Russian Federation"))
institute_list.append(("NRCN", "Nuclear Research Center - Negev, Physics Dept., Beer-Sheva, Israel"))
institute_list.append(("NTHU", "National Tsing Hua University, Hsinchu, Taiwan"))
institute_list.append(("NTU", "National Taiwan University, Taipei, Taiwan"))
institute_list.append(("ODU", "Old Dominion University, Department of Physics, Norfolk VA, USA"))
institute_list.append(("Ohio", "Ohio University, Dept. Of Physics and Astronomy, Athens OH, USA"))
institute_list.append(("ORNL", "Oak Ridge National Laboratory, PO Box 2008, Oak Ridge, TN, USA"))
institute_list.append(("PNNL", "Pacific Northwest National Laboratory, Richland, WA, USA"))
institute_list.append(("Pusan", "Pusan National University, Busan, Republic of Korea"))
institute_list.append(("Rice", "Rice University, Houston, TX, USA"))
institute_list.append(("RIKEN", "RIKEN Nishina Center, Wako, Saitama, Japan"))
institute_list.append(("Rutgers", "Rutgers, The State University of New Jersey, Department of Physics and Astronomy, Piscataway, NJ, USA"))
institute_list.append(("Saha", ""))
institute_list.append(("CFNS", "Center for Frontiers in Nuclear Science, Department of Physics and Astronomy, Stony Brook University, Stony Brook, NY, USA"))
institute_list.append(("StonyBrook", "Department of Physics and Astronomy, Stony Brook University, Stony Brook, NY, USA"))
institute_list.append(("RBRC", "RIKEN BNL Research Center, Brookhaven National Laboratory, Upton, NY, USA"))
institute_list.append(("SCNU", "South China Normal University, Guangzhou, China"))
institute_list.append(("Seoul", "Seoul National University, Seoul, Republic of Korea"))
institute_list.append(("Sejong", "Sejong University, Seoul, Republic of Korea"))
institute_list.append(("Shinshu", "Shinshu University, Matsumoto, Nagano, Japan"))
institute_list.append(("Sungkyunkwan", "Sungkyunkwan University, Suwon, Republic of Korea"))
institute_list.append(("TAU", "Tel Aviv University, Tel Aviv, Israel"))
institute_list.append(("Tokyo", "Tokyo Metropolitan University, Tokyo, Japan"))
institute_list.append(("Tsinghua", "Tsinghua University, Beijing, China"))
institute_list.append(("Tsukuba", "Tsukuba University of Technology, Tsukuba, Japan."))
institute_list.append(("CUBoulder", "University of Colorado Boulder, Boulder, CO, USA"))
institute_list.append(("UCAD", "Universite Cheikh Anta Diop, Dakar, Senegal"))
institute_list.append(("UConn", "University of Connecticut, Storrs, CT, USA"))
institute_list.append(("UH", "University of Houston, Houston, TX, USA"))
institute_list.append(("UIUC", "University of Illinois, Urbana, IL, USA"))
institute_list.append(("UKansas", "University of Kansas, Lawrence, KS, USA"))
institute_list.append(("UKY", "University of Kentucky, Lexington, KY, USA"))
institute_list.append(("Ljubljana", "Faculty of Mathematics and Physics, University of Ljubljana, Ljubljana, Slovenia"))
institute_list.append(("NorthernGeorgia", "University of North Georgia, Dahlonega, GA, USA"))
institute_list.append(("NewHampshire", "University of New Hampshire, Durham, NH, USA"))
institute_list.append(("Oslo", "Department of Physics, University of Oslo, Oslo, Norway"))
institute_list.append(("Regina", "University of Regina, Regina, SK, Canada"))
institute_list.append(("USeoul", "University of Seoul, Seoul, Republic of Korea"))
institute_list.append(("USTC", "University of Science and Technology of China, Hefei, China"))
institute_list.append(("UTAustin", "The University of Texas at Austin, Austin, TX, USA "))
institute_list.append(("UTsukuba", "University of Tsukuba, Tsukuba, Japan"))
institute_list.append(("UTK", "University of Tennessee, Knoxville, TN, USA"))
institute_list.append(("UTSM", ""))
institute_list.append(("UVA", "University of Virginia, Charlottesville, VA, USA"))
institute_list.append(("Vanderbilt", "Department of Physics and Astronomy, Vanderbilt University, Nashville, TN, USA"))
institute_list.append(("VirginiaTech", "Virginia Tech, Blacksburg, VA, USA"))
institute_list.append(("VirginiaUnion", "Virginia Union University, Richmond, VA, USA"))
institute_list.append(("WayneState", "Wayne State University, Detroit, MI, USA"))
institute_list.append(("WI", "Department of Particle Physics and Astrophysics, Weizmann Institute of Science, Rehovot, Israel"))
institute_list.append(("WandM", "William and Mary, Williamsburg, VA, USA"))
institute_list.append(("Yamagata", "Faculty of Science, Yamagata University, Yamagata, Japan"))
institute_list.append(("Yarmouk", "Yarmouk University, Irbid, Jordan"))
institute_list.append(("Yonsei", "Yonsei University, Seoul, Republic of Korea"))
institute_list.append(("York", "University of York, York, UK"))
institute_list.append(("Zagreb", "Department of Physics, Faculty of Science, University of Zagreb, Zagreb, Croatia"))
institute_list.append(("EICJLab", "EIC Center, Thomas Jefferson National Accelerator Facility, Newport News, VA, USA"))

association_list.append(("JLabFellow", "Postdoctoral Fellow at the Jefferson Lab Electron-Ion Collider Center"))
association_list.append(("JLabAward", "Postdoctoral Award for Jefferson Science Associates"))

author_list.append(("MoreheadState", "J. K. Adkins"))
author_list.append(("RIKEN", "Y. Akiba"))
author_list.append(("UKansas", "A. Albataineh"))
author_list.append(("ODU", "M. Amaryan"))
author_list.append(("Oslo", "I. C. Arsene"))
author_list.append(("Sungkyunkwan", "J. Bae"))
author_list.append(("UVA", "X. Bai"))
author_list.append(("Yonsei", "M. Bashkanov"))
author_list.append(("UH", "R. Bellwied"))
author_list.append(("Duquesne", "F. Benmokhtar"))
author_list.append(("CFNS, StonyBrook, RBRC", "J. C. Bernauer"))
author_list.append(("ORNL", "F. Bock"))
author_list.append(("FIU", "W. Boeglin"))
author_list.append(("WI", "M. Borysova"))
author_list.append(("CNU", "E. Brash"))
author_list.append(("JLab", "P. Brindza"))
author_list.append(("GWU", "W. J. Briscoe"))
author_list.append(("LANL", "M. Brooks"))
author_list.append(("ODU", "S. Bueltmann"))
author_list.append(("JazanUniversity", "M. H. S. Bukhari"))
author_list.append(("UKansas", "A. Bylinkin"))
author_list.append(("UConn", "R. Capobianco"))
author_list.append(("AcademiaSinica", "W.-C. Chang"))
author_list.append(("CCNU", "K. Chen"))
author_list.append(("NTU", "K.-F. Chen"))
author_list.append(("NCU", "K.-Y. Cheng"))
author_list.append(("Sejong", "Y. Cheon"))
author_list.append(("BNL", "M. Chiu"))
author_list.append(("UTsukuba", "T. Chujo"))
author_list.append(("BGU", "Z. Citron"))
author_list.append(("CFNS, StonyBrook", "E. Cline"))
author_list.append(("NRCN", "E. Cohen"))
author_list.append(("ORNL", "T. Cormier"))
author_list.append(("LANL", "Y. Corrales Morales"))
author_list.append(("UVA", "C. Cotton"))
author_list.append(("UKY", "C. Crawford"))
author_list.append(("ORNL", "S. Creekmore"))
author_list.append(("JLab", "C.Cuevas"))
author_list.append(("ORNL", "J. Cunningham"))
author_list.append(("BNL", "G. David"))
author_list.append(("LANL", "C. T. Dean"))
author_list.append(("ORNL", "M. Demarteau"))
author_list.append(("UConn", "S. Diehl"))
author_list.append(("Yamagata", "N. Doshita"))
author_list.append(("IJCLabOrsay", "R. Dupr\\'{{e}}"))
author_list.append(("LANL", "J. M. Durham"))
author_list.append(("GSI", "R. Dzhygadlo"))
author_list.append(("ORNL", "R. Ehlers"))
author_list.append(("MSU", "L. El Fassi"))
author_list.append(("UVA", "A. Emmert"))
author_list.append(("JLab", "R. Ent"))
author_list.append(("MIT", "C. Fanelli"))
author_list.append(("UKY", "R. Fatemi"))
author_list.append(("Yonsei", "S. Fegan"))
author_list.append(("Charles", "M. Finger"))
author_list.append(("Charles", "M. Finger Jr."))
author_list.append(("Ohio", "J. Frantz"))
author_list.append(("HUJI", "M. Friedman"))
author_list.append(("Zagreb", "I. Friscic"))
author_list.append(("UH", "D. Gangadharan"))
author_list.append(("Glasgow", "S. Gardner"))
author_list.append(("Glasgow", "K. Gates"))
author_list.append(("Rice", "F. Geurts"))
author_list.append(("Rutgers", "R. Gilman"))
author_list.append(("Glasgow", "D. Glazier"))
author_list.append(("ORNL", "E. Glimos"))
author_list.append(("RIKEN", "Y. Goto"))
author_list.append(("AUGIE", "N. Grau"))
author_list.append(("Vanderbilt", "S. V. Greene"))
author_list.append(("IMP", "A. Q. Guo"))
author_list.append(("FIU", "L. Guo"))
author_list.append(("Yarmouk", "S. K. Ha"))
author_list.append(("BNL", "J. Haggerty"))
author_list.append(("UConn", "T. Hayward"))
author_list.append(("GeorgiaState", "X. He"))
author_list.append(("MIT", "O. Hen"))
author_list.append(("JLab", "D. Higinbotham"))
author_list.append(("IJCLabOrsay", "M. Hoballah"))
author_list.append(("AANL", "A. Hoghmrtsyan"))
author_list.append(("KoreaUniversity", "B. Hong"))
author_list.append(("NTHU", "P.-h. J. Hsu"))
author_list.append(("BNL", "J. Huang"))
author_list.append(("Regina", "G. Huber"))
author_list.append(("UH", "A. Hutson"))
author_list.append(("Yarmouk", "K. Y. Hwang"))
author_list.append(("ODU", "C. Hyde"))
author_list.append(("Tsukuba", "M. Inaba"))
author_list.append(("Yamagata", "T. Iwata"))
author_list.append(("Kyungpook", "H.-S. Jo"))
author_list.append(("UConn", "K. Joo"))
author_list.append(("VirginiaUnion", "N. Kalantarians"))
author_list.append(("Shinshu", "K. Kawade"))
author_list.append(("Regina", "S. Kay"))
author_list.append(("UConn", "A. Kim"))
author_list.append(("Sungkyunkwan", "B. Kim"))
author_list.append(("Pusan", "C. Kim"))
author_list.append(("JeonbukNational", "E.-J. Kim"))
author_list.append(("RIKEN", "M. Kim"))
author_list.append(("Pusan", "Y. Kim"))
author_list.append(("Sejong", "Y. Kim"))
author_list.append(("BNL", "E. Kistenev"))
author_list.append(("UConn", "V. Klimenko"))
author_list.append(("Seoul", "S. H. Ko"))
author_list.append(("MIT", "I. Korover"))
author_list.append(("UKY", "W. Korsch"))
author_list.append(("UKansas", "G. Krintiras"))
author_list.append(("ODU", "S. Kuhn"))
author_list.append(("NCU", "C.-M. Kuo"))
author_list.append(("MIT", "T. Kutz"))
author_list.append(("Inha", "M. Kweon"))
author_list.append(("IowaState", "J. Lajoie"))
author_list.append(("JLab", "D. Lawrence"))
author_list.append(("IowaState", "S. Lebedev"))
author_list.append(("Seoul", "J. S. H. Lee"))
author_list.append(("Kyungpook", "S. W. Lee"))
author_list.append(("MIT", "Y.-J. Lee"))
author_list.append(("SCNU", "H. Li"))
author_list.append(("Rice", "W. Li"))
author_list.append(("CFNS, EICJLab, StonyBrook, WandM, JLabAward, JLabFellow", "W. Li"))
author_list.append(("CIAE", "X. Li"))
author_list.append(("LANL", "X. Li"))
author_list.append(("USTC", "X. Li"))
author_list.append(("IMP", "Y. T. Liang"))
author_list.append(("Pusan", "S. Lim"))
author_list.append(("AcademiaSinica", "C.-h. Lin"))
author_list.append(("IMP", "D. X. Lin"))
author_list.append(("SCNU", "G. Liu"))
author_list.append(("LANL", "K. Liu"))
author_list.append(("LANL", "M. X. Liu"))
author_list.append(("Glasgow", "K. Livingston"))
author_list.append(("UVA", "N. Liyanage"))
author_list.append(("WayneState", "W. J. Llope"))
author_list.append(("ORNL", "C. Loizides"))
author_list.append(("NewHampshire", "E. Long"))
author_list.append(("NTU", "R.-S. Lu"))
author_list.append(("CIAE", "Z. Lu"))
author_list.append(("Yonsei", "W. Lynch"))
author_list.append(("IJCLabOrsay", "D. Marchand"))
author_list.append(("CzechTechUniv", "M. Marcisovsky"))
author_list.append(("FIU", "P. Markowitz"))
author_list.append(("AANL", "H. Marukyan"))
author_list.append(("LANL", "P. McGaughey"))
author_list.append(("Ljubljana", "M. Mihovilovic"))
author_list.append(("MIT", "R. G. Milner"))
author_list.append(("WI", "A. Milov"))
author_list.append(("Yamagata", "Y. Miyachi"))
author_list.append(("AANL", "A. Mkrtchyan"))
author_list.append(("AANL", "H. Mkrtchyan"))
author_list.append(("CNU", "P. Monaghan"))
author_list.append(("Glasgow", "R. Montgomery"))
author_list.append(("BNL", "D. Morrison"))
author_list.append(("AANL", "A. Movsisyan"))
author_list.append(("IJCLabOrsay", "C. Munoz Camacho"))
author_list.append(("UKansas", "M. Murray"))
author_list.append(("LANL", "K. Nagai"))
author_list.append(("CUBoulder", "J. Nagle"))
author_list.append(("RIKEN", "I. Nakagawa"))
author_list.append(("UTK", "C. Nattrass"))
author_list.append(("JLab", "D. Nguyen"))
author_list.append(("IJCLabOrsay", "S. Niccolai"))
author_list.append(("BNL", "R. Nouicer"))
author_list.append(("RIKEN", "G. Nukazuka"))
author_list.append(("UVA", "M. Nycz"))
author_list.append(("NRNUMEPhI", "V. A. Okorokov"))
author_list.append(("Regina", "S. Ore$\\check{{s}}$i$\\acute{{c}}$"))
author_list.append(("ORNL", "J. Osborn"))
author_list.append(("LANL", "C. O'Shaughnessy"))
author_list.append(("NTU", "S. Paganis"))
author_list.append(("Regina", "Z Papandreou"))
author_list.append(("NMSU", "S. Pate"))
author_list.append(("IowaState", "M. Patel"))
author_list.append(("MIT", "C. Paus"))
author_list.append(("Glasgow", "G. Penman"))
author_list.append(("UIUC", "M. G. Perdekamp"))
author_list.append(("CUBoulder", "D. V. Perepelitsa"))
author_list.append(("LANL", "H. Periera da Costa"))
author_list.append(("GSI", "K. Peters"))
author_list.append(("CNU", "W. Phelps"))
author_list.append(("TAU", "E. Piasetzky"))
author_list.append(("BNL", "C. Pinkenburg"))
author_list.append(("Charles", "I. Prochazka"))
author_list.append(("LehighUniversity", "T. Protzman"))
author_list.append(("BNL", "M. Purschke"))
author_list.append(("WayneState", "J. Putschke"))
author_list.append(("MIT", "J. R. Pybus"))
author_list.append(("JLab", "R. Rajput-Ghoshal"))
author_list.append(("ORNL", "J. Rasson"))
author_list.append(("FIU", "B. Raue"))
author_list.append(("ORNL", "K. Read"))
author_list.append(("LehighUniversity", "R. Reed"))
author_list.append(("FIU", "J. Reinhold"))
author_list.append(("LANL", "E. L. Renner"))
author_list.append(("UConn", "J. Richards"))
author_list.append(("UIUC", "C. Riedl"))
author_list.append(("BNL", "T. Rinn"))
author_list.append(("Ohio", "J. Roche"))
author_list.append(("Oslo", "K. R$\\o$ed"))
author_list.append(("MIT", "G. M. Roland"))
author_list.append(("HUJI", "G. Ron"))
author_list.append(("IowaState", "M. Rosati"))
author_list.append(("UKansas", "C. Royon"))
author_list.append(("Pusan", "J. Ryu"))
author_list.append(("Rutgers", "S. Salur"))
author_list.append(("MIT", "N. Santiesteban"))
author_list.append(("UConn", "R. Santos"))
author_list.append(("GeorgiaState", "M. Sarsour"))
author_list.append(("ORNL", "J. Schambach"))
author_list.append(("GWU", "A. Schmidt"))
author_list.append(("ORNL", "N. Schmidt"))
author_list.append(("GSI", "C. Schwarz"))
author_list.append(("GSI", "J. Schwiening"))
author_list.append(("RIKEN", "R. Seidl"))
author_list.append(("UIUC", "A. Sickles"))
author_list.append(("UConn", "P. Simmerling"))
author_list.append(("Ljubljana", "S. Sirca"))
author_list.append(("GeorgiaState", "D. Sharma"))
author_list.append(("LANL", "Z. Shi"))
author_list.append(("Nihon", "T.-A. Shibata"))
author_list.append(("NCU", "C.-W. Shih"))
author_list.append(("RIKEN", "S. Shimizu"))
author_list.append(("UConn", "U. Shrestha"))
author_list.append(("NewHampshire", "K. Slifer"))
author_list.append(("LANL", "K. Smith"))
author_list.append(("LLNL", "R. Soltz"))
author_list.append(("LANL", "W. Sondheim"))
author_list.append(("CIAE", "J. Song"))
author_list.append(("Pusan", "J. Song"))
author_list.append(("BNL", "P. Steinberg"))
author_list.append(("WandM", "J. Stevens"))
author_list.append(("GWU", "I. I. Strakovsky"))
author_list.append(("PNNL", "J. Strube"))
author_list.append(("CIAE", "P. Sun"))
author_list.append(("CCNU", "X. Sun"))
author_list.append(("Regina", "K. Suresh"))
author_list.append(("AANL", "A. Tadevosyan"))
author_list.append(("NCU", "W.-C. Tang"))
author_list.append(("IowaState", "S. Tapia Araya"))
author_list.append(("Vanderbilt", "S. Tarafdar"))
author_list.append(("BrunelUniversity", "L. Teodorescu"))
author_list.append(("UH", "A. Timmins"))
author_list.append(("CzechTechUniv", "L. Tomasek"))
author_list.append(("UConn", "N. Trotta"))
author_list.append(("Oslo", "T. S. Tveter"))
author_list.append(("IowaState", "E. Umaka"))
author_list.append(("Regina", "A. Usman"))
author_list.append(("LANL", "H. W. Van Hecke"))
author_list.append(("EICJLab, IJCLabOrsay, JLabFellow", "C. Van Hulse"))
author_list.append(("Vanderbilt", "J. Velkovska"))
author_list.append(("IJCLabOrsay", "E. Voutier"))
author_list.append(("IJCLabOrsay", "P.K. Wang"))
author_list.append(("UKansas", "Q. Wang"))
author_list.append(("CCNU", "Y. Wang"))
author_list.append(("Tsinghua", "Y. Wang"))
author_list.append(("Yonsei", "D. P. Watts"))
author_list.append(("ODU", "L. Weinstein"))
author_list.append(("MIT", "M. Williams"))
author_list.append(("LANL", "C.-P. Wong"))
author_list.append(("PNNL", "L. Wood"))
author_list.append(("CanisiusCollege", "M. H. Wood"))
author_list.append(("BNL", "C. Woody"))
author_list.append(("MIT", "B. Wyslouch"))
author_list.append(("Tsinghua", "Z. Xiao"))
author_list.append(("KobeUniversity", "Y. Yamazaki"))
author_list.append(("SCNU", "S. Yang"))
author_list.append(("NCKU", "Y. Yang"))
author_list.append(("Tsinghua", "Z. Ye"))
author_list.append(("Yarmouk", "H. D. Yoo"))
author_list.append(("LANL", "M. Yurov"))
author_list.append(("Yonsei", "N. Zachariou"))
author_list.append(("Columbia", "W.A. Zajc"))
author_list.append(("USTC", "W. Zha"))
author_list.append(("UVA", "J. Zhang"))
author_list.append(("Tsinghua", "Y. Zhang"))
author_list.append(("USTC", "Y. Zhang"))
author_list.append(("IMP", "Y. X. Zhao"))
author_list.append(("UVA", "X. Zheng"))
author_list.append(("USTC", "S. Zhu"))
author_list.append(("Tsinghua", "P. Zhuang"))
author_list.append(("CUA", ""))
author_list.append(("Duke", ""))
author_list.append(("Hampton", ""))
author_list.append(("HEAROKEK", ""))
author_list.append(("Inha", ""))
author_list.append(("IPAS", ""))
author_list.append(("JAEA", ""))
author_list.append(("JeonbukNational", ""))
author_list.append(("JMU", ""))
author_list.append(("LBNL", ""))
author_list.append(("Saha", ""))
author_list.append(("Tokyo", ""))
author_list.append(("UCAD", ""))
author_list.append(("NorthernGeorgia", ""))
author_list.append(("UTAustin", ""))
author_list.append(("UTSM", ""))
author_list.append(("VirginiaTech", ""))

institute_list.sort(key=lambda x:x[1])
association_list.sort(key=lambda x:x[1])
author_list.sort(key=lambda x:x[1].split(" ")[-1])

author_file = open("{}/author_list.tex".format(os.getcwd()), "w")
author_file.write("% {}\n\n".format(generation_time))

for institute_number, institute in enumerate(institute_list):
	author_file.write('\\newcommand\\{0}[1] {{\\ifnum#1=1 {1}\\else {2}\\fi}}\n'.format(institute[0], institute_number + 1, institute[1]))

for letter, institute in zip(ascii_lowercase, association_list):
	author_file.write('\n\\newcommand\\{0}[1] {{\\ifnum#1=1 {1}\\else {2}\\fi}}'.format(institute[0], letter, institute[1]))

author_file.write("\n\n\n")

for author in author_list:
	author_file.write('\\author[\\{}{{1}}]{{{}}}\n'.format(author[0].replace(", ", "{1},~\\"), author[1].replace(" ", "~")))

author_file.write("\n\n\\renewcommand\\Affilfont{\\itshape\\small}\n")

for institute in institute_list:
	author_file.write('\\affil[\\{}{{1}}]{{\\{}{{2}}}}\n'.format(institute[0], institute[0]))

for institute in association_list:
	author_file.write('\\affil[\\{}{{1}}]{{\\{}{{2}}}}\n'.format(institute[0], institute[0]))

author_file.close()