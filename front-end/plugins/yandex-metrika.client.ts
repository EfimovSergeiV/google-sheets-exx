export default defineNuxtPlugin((nuxtApp) => {
  if (process.client) {
    (window as any).ym = (window as any).ym || function (...args: any[]) {
      ((window as any).ym.a = (window as any).ym.a || []).push(args);
    };
    (window as any).ym.l = +new Date();

    (window as any).ym(101988467, 'init', {
      clickmap: true,
      trackLinks: true,
      accurateTrackBounce: true,
      webvisor: true
    });

    // Добавляем метод reachGoal в NuxtApp
    nuxtApp.provide('metrika', {
      reachGoal: (target: string, params?: Record<string, any>) => {
        try {
          (window as any).ym(101988467, 'reachGoal', target, params || {});
        } catch (e) {
          console.warn('Yandex Metrika error:', e);
        }
      }
    });
  }
});