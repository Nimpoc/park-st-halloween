"""Cache Halloween airport observations; never substitute modelled weather."""
import csv, io, json, pathlib, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
def fetch(year):
    params = [('station','BLI'),('data','tmpf'),('data','sknt'),('data','p01i'),('data','metar'),
              ('year1',str(year)),('month1','10'),('day1','31'),('year2',str(year)),('month2','11'),('day2','1'),
              ('tz','America/Los_Angeles'),('format','onlycomma'),('latlon','no'),('elev','no'),
              ('missing','M'),('trace','T'),('direct','no'),('report_type','3')]
    url = 'https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?' + urllib.parse.urlencode(params)
    try:
        raw = urllib.request.urlopen(url, timeout=50).read().decode()
        if not raw.startswith('station,valid,'): raise ValueError('Unexpected response')
        (ROOT/'data'/f'airport-{year}.csv').write_text(raw)
        rows = list(csv.DictReader(io.StringIO(raw)))
        observations = []
        for r in rows:
            # Routine hourly reports only: no duplicate precipitation totals from special METARs.
            if r['valid'][11:13] not in ['17','18','19','20','21']: continue
            def num(k):
                try: return float(r[k])
                except ValueError: return None
            observations.append({'time':r['valid'][11:16], 'temperatureF':num('tmpf'),
                'windMph':round(num('sknt')*1.15078,1) if num('sknt') is not None else None,
                'precipIn':num('p01i'), 'trace':r['p01i']=='T', 'metar':r['metar']})
        return str(year), {'station':'KBLI · Bellingham International Airport', 'url':url,
            'date':f'{year}-10-31','timezone':'America/Los_Angeles','observations':observations,
            'status':'available' if observations else 'unavailable'}
    except Exception as e:
        return str(year), {'station':'KBLI · Bellingham International Airport','url':url,'observations':[],
            'status':'unavailable','error':str(e)}

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool: results = dict(pool.map(fetch,range(2010,2027)))
    out={'source':'Iowa Environmental Mesonet / ASOS archive','retrievedAt':datetime.now(timezone.utc).isoformat(),
         'method':'Routine hourly METAR reports timestamped 17:00–21:59 local time on October 31. Temperatures and winds are observations, not daily extrema. Precipitation is reported preceding-hour accumulation; trace retained separately. Missing reports remain missing.',
         'years':results}
    (ROOT/'data'/'weather.json').write_text(json.dumps(out,indent=2))
    print('\n'.join(f'{y}: {len(v["observations"])} evening reports ({v["status"]})' for y,v in sorted(results.items())))
