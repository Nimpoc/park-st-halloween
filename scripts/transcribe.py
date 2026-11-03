import json, pathlib, shutil, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'data/records.json').read_text()); by={r['year']:r for r in rows}
if len(sys.argv)!=2: raise SystemExit('Usage: python3 scripts/transcribe.py /path/to/source_scans')
scans=pathlib.Path(sys.argv[1])
(ROOT/'sources').mkdir(exist_ok=True)
files={2026:'IMG_8848.JPEG',2025:'IMG_5596(1).jpeg',2024:'IMG_5597(1).jpeg',2023:'IMG_5598(1).jpeg',2022:'IMG_5599(1).jpeg',2021:'IMG_5600(1).jpeg',2019:'IMG_5601(1).jpeg',2018:'IMG_5602(1).jpeg',2017:'IMG_5603(1).jpeg',2016:'IMG_5604(1).jpeg',2015:'IMG_5605(1).jpeg',2014:'IMG_5606.jpeg',2012:'IMG_5607.jpeg',2011:'IMG_5608.jpeg',2010:'IMG_5610.jpeg'}
for y,f in files.items():
 dest=f'{y}.jpg';shutil.copyfile(scans/f,ROOT/'sources'/dest)
 by[y]['sourceImages']=[{'name':f,'src':'sources/'+dest}]
 by[y]['provenance']='Visual transcription from the original scan; see reconciliation notes. Blank rows are omitted, not assumed zero. Isolated time labels are treated as interval starts; durations follow the sheet cadence unless noted.'
 by[y]['confidence']='medium'
shutil.copyfile(scans/'IMG_5609.jpeg',ROOT/'sources/2011-detail.jpg')
by[2011]['sourceImages'].append({'name':'IMG_5609.jpeg (detail of the same sheet)','src':'sources/2011-detail.jpg'})
def points(y,start,counts,step=15):
 by[y]['intervals']=[{'time':f'{(start+i*step)//60:02}:{(start+i*step)%60:02}','count':n,'minutes':step} for i,n in enumerate(counts) if n is not None]
def note(y,s):by[y]['notes']=s
points(2010,17*60,[2,1,4,18,21,32,12,11,6,9,7,5],20)
points(2011,17*60,[None,1,None,1,1,13,None,8,22,None,3,33,None,7,None])
by[2011]['confidence']='low';by[2011]['sourceApproximate']=True
note(2011,'Damaged, faded pink-ink sheet. Circled figures read 137 / 138; 138 is retained as an approximate written total. Only legible individual time rows are plotted; 6:30, 7:15, 8:00 and 8:30 remain unresolved. The second image is a close-up of this same sheet, not an extra year. Scribbled-out tallies at 6:45 are excluded.')
by[2011]['handwrittenWeather']='Faded weather heading is not legible enough to transcribe.'
points(2012,17*60+30,[4,1,7,18,4,30,3,4,9,11,10,4,2])
by[2012]['handwrittenWeather']='“windy, rain, not super cold / phone says 59°” · “Very windy”'
points(2014,17*60+45,[2,None,15,17,29,26,18,11,3,9,11,None,None,2])
by[2014]['handwrittenWeather']='“Clear, rainy earlier in the day”'
points(2015,17*60+30,[2,4,28,17,28,6,20,17,4,7,7,5,3,3])
by[2015]['sourceTotal']=None;by[2015]['estimate']=151;by[2015]['status']='reconstructed';by[2015]['confidence']='low'
note(2015,'The visible tally rows sum to 151. The circled arithmetic at the lower right is clipped: 126, 32 and a further partly cut-off figure are visible. There is no fully legible authoritative annual total, so 151 is an interval-derived estimate. Earlier transcription left the year blank. The porch note says they got home at 5:30 to start tending the door.')
by[2015]['handwrittenWeather']='“Crazy rain earlier, then clear for trick or treaters”'
points(2016,17*60+30,[29,13,72,48,33],30)
# The final entry says only 8:30; its duration is not established, so retain as an untimed count.
by[2016]['untimedCounts']=[{'label':'8:30 (duration unspecified)','count':13}]
note(2016,'“Note: few kids went Twizzlers, most kids seek chocolate.” Explicit half-hour intervals total 195. The final “8:30” tally is 13, bringing all tallies to the written 208. Its duration is unspecified, so it is retained separately and excluded from the time curve rather than given an invented duration.')
by[2017]['intervals']=[{'time':t,'count':n,'minutes':m} for t,n,m in [('17:45',4,15),('18:00',55,30),('18:30',46,30),('19:00',35,30),('19:30',8,30),('20:00',20,30),('20:30',6,30),('21:00',4,30)]]
by[2017]['notes']='Jessie in Mexico, Ashley + Tele on candy duty. Pretzels 2017!\n\nKid: “What’re these?”\nAsh: “They’re pretzels! … Salty is very good w/ sweet, you may understand that when you’re older.”\n\n“Thats a nice costume for a mermaid!”\nMe: “Nice doctor costume!”\nKid: “Yeah, I really like being a doctor but it wasn’t the right costume!”\nKid: “I got worms!”\nAlso, a T-Rex that barely cleared the porch.\n\nReconciliation: written total 174 excludes the final four tallies at 9:00. All time rows sum to 178. Final 9:00 duration follows the preceding 30-minute cadence.'
points(2018,17*60,[6,7,6,17,10,27,17,43,40,32,37,13,None,10,None,None,3])
points(2019,16*60+30,[3,None,None,None,4,9,26,15,22,53,22,35,15,11,40,5,9])
note(2019,'“Clear” · “(dusk)” is written near 6:00. The early tally at 4:30 reads 3, while a nearby pencil subtotal reads 6. The visible individual rows sum to 269; the circled annual total is 268. Both are preserved. Crossed-out extra marks at 7:30 are excluded.')
points(2021,16*60+45,[3,16,25,25,21,35,40,37,19,37,35,12,11,7,8,None,2,None,8])
note(2021,'“Deb!! gives bracelets (Napoleon dynamite)”\n“Zoom teacher — girl w/ cardboard computer frame, PJ bottoms + fluffy slippers!”\n\nThe handwritten numeric interval subtotals reconcile to 341. Blank rows at 8:30 and 9:00 are unfilled, not verified zeros.')
points(2022,16*60+15,[4,None,3,2,2,3,11,28,24,33,30,42,45,36,21,5,2,2])
note(2022,'All visible tally rows total 293, including 7 visitors before 5:00. The written annual total is 286; excluding those 7 early arrivals reconciles it exactly. Both the written total and the full interval series are retained.')
points(2023,17*60+45,[8,21,42,31,16,6,48,29,3,13,4,2])
note(2023,'Circled annual total: 259. Visible tally interpretation: 223. The first row at 5:45 visibly has 8 marks but its pencil margin says 13; the 7:15 numeric margin says 48 (dense tallies), retained here. Even using the first margin 13 gives 228, so the written total cannot be reconciled from the visible rows. The 8:15 and 8:30 rows contain 4 and 2 marks; their combined margin is 6. This curve is uncertain, not adjusted to force 259.')
by[2023]['confidence']='low'
points(2024,17*60+15,[3,None,17,50,40,35,21,34,24,36,45,10,None,16])
by[2024]['confidence']='high';by[2024]['handwrittenWeather']='“Balmy 47°; ‘not raining, really’ — Ashley”'
note(2024,'“Carrots — Huge Hit”\n“Celery — somewhat hit”\n“garlic — good for vampires”\n“tea baggers”\n\nAll transcribed nonblank intervals reconcile exactly to the written 331. Blank rows remain unfilled.')
points(2025,17*60+15,[4,7,7,11,16,23,35,29,15,37,30,10,2,5,None,None,2])
by[2025]['handwrittenWeather']='“weather — rainy + blustery”'
by[2025]['estimate']=231;by[2025]['sourceTotal']=None;by[2025]['confidence']='low'
note(2025,'No legible annual total appears on this sheet. The earlier chat estimated approximately 231; retained as an estimate, not a written total. The current visual interpretation sums to 233. Dense overlapping tallies at 6:45 are read as 35 and remain uncertain. Crossed-out marks at 6:00 are excluded. Blank time rows are not zeros.')
points(2026,17*60,[12,4,26,53,41,43,45,40,48,20,34,35,35,19,12,28,5,2,None,3])
by[2026]['confidence']='high'
by[2026]['notes']='Original IMG_8848.JPEG confirms the written 505 and 19 nonblank time rows. Blank 9:30 is omitted, not a measured zero.'
for r in rows:
 if r['year'] in files:
  r['computedInterpretation']=sum(p['count'] for p in r['intervals']) if r['intervals'] else None
  r['auditStatus']='reviewed-with-uncertainties' if r['confidence']=='low' else 'visually-reviewed'
 else:r['auditStatus']='missing-source';r['provenance']='No sheet supplied for this year.'
 if r['year'] in files and not r['notes']:
  r['notes']='Blank rows are unfilled; only rows with visible tallies are included.'
(ROOT/'data/records.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
for r in rows:print(r['year'],r['sourceTotal'],r['estimate'],r['computedInterpretation'],len(r['intervals']))
