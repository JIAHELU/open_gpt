import { z } from 'zod'

export const createAppSchema = z.object({
  name: z.string().min(1),
  icon: z.string().emoji(),
  demoInput: z.string().min(1),
  prompt: z.string().min(1),
  embedding: z.string().min(1).default("[123]")
})
