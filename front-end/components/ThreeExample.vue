<script setup>
  import { 
    Scene, PerspectiveCamera, WebGLRenderer, 
    AmbientLight, DirectionalLight, Box3, Vector3, PointLight, HemisphereLight,
    PCFSoftShadowMap
  } from 'three'
  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'
  import { OrbitControls } from 'three/addons/controls/OrbitControls.js'

  import { ref, onMounted } from 'vue'

  let renderer, controls, model
  const experience = ref(null)

  const scene = new Scene()

  // свет
  scene.add(new AmbientLight(0x404040, 2))
  const dirLight = new DirectionalLight(0xffffff, 2)
  dirLight.position.set(5, 10, 7.5)
  scene.add(dirLight)

  const point1 = new PointLight(0xffffff, 1.5)
  point1.position.set(-5, 3, 5)
  scene.add(point1)

  const point2 = new PointLight(0xffffff, 0.8)
  point2.position.set(5, 3, 5)
  scene.add(point2)

  const hemiLight = new HemisphereLight(0xffffff, 0x444444, 1)
  hemiLight.position.set(0, 10, 0)
  scene.add(hemiLight)

  // камера
  const camera = new PerspectiveCamera(45, 1, 0.1, 1000)
  camera.position.set(0, 0, 4)
  scene.add(camera)

  // состояние вращения
  const autoRotate = ref(true)
  const targetRotation = ref(null) // конечный угол при клике

  // загрузка модели
  const gltfLoader = new GLTFLoader()
  gltfLoader.load('/PotPlant.glb', (gltf) => {
    model = gltf.scene

    // нормализация размера
    const box = new Box3().setFromObject(model)
    const size = new Vector3()
    box.getSize(size)
    const maxDim = Math.max(size.x, size.y, size.z)
    const scale = 2 / maxDim
    model.scale.setScalar(scale)

    // центрирование
    const center = box.getCenter(new Vector3())
    model.position.sub(center.multiplyScalar(scale))

    scene.add(model)
  })

  // кнопка "поворот на 60°"
  function rotateBy60() {
    if (!model) return
    autoRotate.value = false
    targetRotation.value = model.rotation.y + (Math.PI / 3) // 60°
  }

  // рендерер
  function updateRenderer() {
    renderer.setSize(400, 400)
    renderer.render(scene, camera)
    dirLight.castShadow = true
    renderer.shadowMap.enabled = true
    renderer.shadowMap.type = PCFSoftShadowMap
  }

  function setRenderer() {
    if (experience.value) {
      renderer = new WebGLRenderer({ canvas: experience.value, alpha: true, antialias: true })
      renderer.setClearColor(0x000000, 0)

      controls = new OrbitControls(camera, renderer.domElement)
      controls.enableDamping = true
      controls.dampingFactor = 0.05
      controls.enableZoom = false
      updateRenderer()
    }
  }

  onMounted(() => {
    setRenderer()
    loop()
  })

  const loop = () => {
    if (model) {
      if (autoRotate.value) {
        model.rotation.y += 0.005
      } else if (targetRotation.value !== null) {
        // плавный доворот к цели
        const diff = targetRotation.value - model.rotation.y
        if (Math.abs(diff) > 0.01) {
          model.rotation.y += diff * 0.1
        } else {
          model.rotation.y = targetRotation.value
          targetRotation.value = null
        }
      }
    }

    if (controls) controls.update()
    updateRenderer()
    requestAnimationFrame(loop)
  }
</script>

<template>
  <div class="flex flex-col items-center space-y-4">
    <canvas ref="experience" />

    <div class="space-x-2">
      <button 
        class="px-4 py-2 w-44 bg-blue-500 text-white rounded" 
        @click="autoRotate = true"
      >
        Автовращение
      </button>
      <button 
        class="px-4 py-2 w-44 bg-green-500 text-white rounded" 
        @click="rotateBy60"
      >
        Повернуть
      </button>
    </div>
  </div>
</template>
