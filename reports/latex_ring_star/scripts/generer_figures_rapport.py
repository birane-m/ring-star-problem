"""Optional: regenerate readable report figures from saved data, no solver.

Run with the project's Python environment (Matplotlib required).
"""
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
COLORS = {"greedy":"#2563eb", "local_search":"#d97706", "tabu_search":"#0f766e"}
LABELS = {"greedy":"Construction", "local_search":"Recherche locale", "tabu_search":"Recherche tabou"}
MARKERS = {"greedy":"o", "local_search":"s", "tabu_search":"^"}


def main():
    with (ROOT/'resultats/campagne/summary.csv').open() as f:
        rows=list(csv.DictReader(f))
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":11,
                         "axes.spines.top":False,"axes.spines.right":False,
                         "axes.edgecolor":"#cbd5e1", "pdf.fonttype":42})
    for instance in ["att48","kroA100"]:
        case=[r for r in rows if r['instance']==instance]
        fig,axes=plt.subplots(3,1,figsize=(7.2,6.8))
        for method in COLORS:
            series=sorted([r for r in case if r['method']==method],key=lambda r:int(r['p']))
            xs=[int(r['p']) for r in series]
            kwargs=dict(label=LABELS[method],color=COLORS[method],marker=MARKERS[method],lw=1.8,capsize=3)
            axes[0].errorbar(xs,[float(r['mean_cost']) for r in series],yerr=[float(r['std_cost'] or 0) for r in series],**kwargs)
            axes[1].errorbar(xs,[1000*float(r['mean_seconds']) for r in series],yerr=[1000*float(r['std_seconds'] or 0) for r in series],**kwargs)
            if method!='greedy':
                base={int(r['p']):float(r['mean_cost']) for r in case if r['method']=='greedy'}
                axes[2].errorbar(xs,[100*(base[int(r['p'])]-float(r['mean_cost']))/base[int(r['p'])] for r in series],yerr=[100*float(r['std_cost'] or 0)/base[int(r['p'])] for r in series],**kwargs)
        for ax in axes:
            ax.set_xticks([3,5,10]);ax.set_xlabel('Nombre de stations p');ax.grid(axis='y',alpha=.2)
        axes[0].set_ylabel('Coût total moyen');axes[0].legend(frameon=False,fontsize=9,ncol=3,loc='upper right')
        axes[1].set_ylabel('Temps moyen (ms)');axes[1].set_yscale('log')
        axes[2].set_ylabel('Gain moyen (%)');axes[2].axhline(0,color='#94a3b8',lw=.7)
        fig.suptitle(f"{instance} · n={case[0]['n']} · α=1",weight='bold',y=.995,fontsize=14)
        fig.text(.08,.008,'Moyennes et écarts-types observés ; trois graines pour les recherches.\nPLNE ignorée selon les limites de taille configurées.',fontsize=9,color='#62666a')
        fig.tight_layout(rect=(0,.07,1,.98),h_pad=.8)
        fig.savefig(ROOT/f'figures/comparaison_{instance}.pdf',bbox_inches='tight');plt.close(fig)
    data=json.loads((ROOT/'resultats/exemple_att48/solution.json').read_text())
    fig,axes=plt.subplots(2,1,figsize=(7.2,5.6))
    for ax,field,label in zip(axes,['evaluations','elapsed_seconds'],["Nombre d'évaluations","Temps d'amélioration (s)"]):
        hist=data['history'];x=[r[field] for r in hist]
        ax.plot(x,[r['current_cost'] for r in hist],color='#94a3b8',lw=1,label='Solution courante')
        ax.step(x,[r['best_cost'] for r in hist],where='post',color='#0f766e',lw=2,label='Meilleur coût')
        ax.set_xlabel(label);ax.set_ylabel('Coût total');ax.grid(axis='y',alpha=.2)
    axes[0].legend(frameon=False,fontsize=9,loc='upper right')
    fig.tight_layout(h_pad=1.3)
    fig.savefig(ROOT/'figures/convergence_att48.pdf',bbox_inches='tight');plt.close(fig)


if __name__=='__main__':main()
