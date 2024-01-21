const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/IndexPage.vue") }],
  },

  {
    path: "/login",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/LoginPage.vue") }],
  },
  {
    path: "/signup",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/SignUpPage.vue") }],
  },
  {
    path: "/schedule",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/SchedulePage.vue") }],
  },

  

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
